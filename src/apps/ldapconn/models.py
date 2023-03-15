import struct
import uuid
import binascii
import ldap
from ldap import modlist

from django.db import transaction
from apps.lnxusers.models import LnxUser, LnxGroup, LnxShell
from .ldap import LDAPObjectsService


class LDAPHelper:

    list_fields = (
        'member',
        'memberOf',
        'sudoCommand',
        'sudoHost',
        'sudoOption',
        'sudoUser',
    )

    def _get_ldap_values(self, attrs_val, key):
        if len(attrs_val) > 1 or key in self.list_fields:
            return [val.decode('utf-8') for val in attrs_val]
        else:
            return attrs_val[0].decode('utf-8')

    def get_attributes(self, attrs, key):
        if key in attrs:
            output = self._get_ldap_values(attrs[key], key)
        else:
            output = ''
        return output

    def _sid_to_string(self, binary):
        version = struct.unpack('B', binary[0:1])[0]
        # I do not know how to treat version != 1 (it does not exist yet)
        assert version == 1, version
        length = struct.unpack('B', binary[1:2])[0]
        authority = struct.unpack(b'>Q', b'\x00\x00' + binary[2:8])[0]
        string = f"S-{version}-{authority}"
        binary = binary[8:]
        assert len(binary) == 4 * length
        for i in range(length):
            value = struct.unpack('<L', binary[4*i:4*(i+1)])[0]
            string += f"-{value}"
        return string

    def get_sid(self, attrs, key):
        if key in attrs:
            return self._sid_to_string(attrs[key][0])
        else:
            return 'N/A'

    def get_guid(self, attrs, key):
        if key in attrs:
            val = uuid.UUID(bytes_le=attrs[key][0])
            return str(val).lower()
        else:
            return 'N/A'

    def get_guid_hex(self, attrs, key):
        if key in attrs:
            return binascii.hexlify(attrs[key][0]).decode('utf-8')
        else:
            return 'N/A'


class LDAPUser:

    def __init__(self, dn, attrs):
        helper = LDAPHelper()
        self.distinguishedName = dn
        self.name = helper.get_attributes(attrs, 'name')
        self.userPrincipalName = helper.get_attributes(attrs, 'userPrincipalName')
        self.cn = helper.get_attributes(attrs, 'cn')
        self.sAMAccountName = helper.get_attributes(attrs, 'sAMAccountName')
        self.givenName = helper.get_attributes(attrs, 'givenName')
        self.sn = helper.get_attributes(attrs, 'sn')
        self.objectSid = helper.get_sid(attrs, 'objectSid')
        self.objectGUID = helper.get_guid(attrs, 'objectGUID')
        self.objectGUIDHex = helper.get_guid_hex(attrs, 'objectGUID')

    @classmethod
    def get_objectclass_filter(cls, guid=None):
        if guid:
            return f"(&(objectClass=Person)(userPrincipalName=*)(objectGUID={guid}))"
        return "(&(objectClass=Person)(userPrincipalName=*))"

    @classmethod
    def get_attributes_list(cls):
        return ['*']

    @classmethod
    def get_dn_to_search(cls, ldap_config):
        return ldap_config.get_user_base_dns()

    @classmethod
    def get_defaults(cls, ldap_config, attrs):
        return ldap_config.get_user_defaults(attrs)

    @classmethod
    def _get_free_id(cls, ldap_config):
        min_id, max_id = ldap_config.get_user_min(), ldap_config.get_user_max()
        pool = set(range(min_id, max_id + 1)) # large pools not accepted

        used_ids = set(LnxUser.objects.values_list('uid_number', flat=True))

        available_uids = pool - used_ids  # Subtract used numbers from pool
        return str(available_uids.pop()).encode('utf-8')

    @classmethod
    def _modify_ldap_entry(cls, ldap_conn, entry_defaults, free_uid, dn):
        mod_attrs = [
            ( ldap.MOD_REPLACE, "gidNumber", entry_defaults['gidNumber']),
            ( ldap.MOD_REPLACE, "uidNumber", free_uid),
            ( ldap.MOD_REPLACE, "gecos", entry_defaults['gecos']),
            ( ldap.MOD_REPLACE, "homeDirectory", entry_defaults['homeDirectory']),
            ( ldap.MOD_REPLACE, "loginShell", entry_defaults['loginShell'])
        ]

        ldap_conn.modify_s(dn, mod_attrs)

    @classmethod
    def _create_db_entry(cls, entry_defaults, guid, free_uid):
        primary_group = LnxGroup.objects.get(
            gid_number=int(entry_defaults['gidNumber'].decode('utf-8')))
        shell = LnxShell.objects.get(
            shell=entry_defaults['loginShell'].decode('utf-8'))
        LnxUser.objects.create(
            username=entry_defaults['uid'].decode('utf-8'),
            uid_number=int(free_uid),
            primary_group=primary_group,
            login_shell=shell,
            home_dir=entry_defaults['homeDirectory'].decode('utf-8'),
            gecos=entry_defaults['gecos'].decode('utf-8')
        )

    @classmethod
    @transaction.atomic
    def perform_create(cls, ldap_config, ldap_conn, dn, entry_defaults, guid):
        free_uid = cls._get_free_id(ldap_config)
        cls._create_db_entry(entry_defaults, guid, free_uid)
        cls._modify_ldap_entry(ldap_conn, entry_defaults, free_uid, dn)

    def apply_filter(self, filter_str):
        return (filter_str in self.distinguishedName or
            filter_str in self.userPrincipalName)


class LDAPGroup:

    def __init__(self, dn, attrs):
        helper = LDAPHelper()
        self.distinguishedName = dn
        self.sAMAccountName = helper.get_attributes(attrs, 'sAMAccountName')
        self.cn = helper.get_attributes(attrs, 'cn')
        self.description = helper.get_attributes(attrs, 'description')
        self.member = helper.get_attributes(attrs, 'member')
        self.memberOf = helper.get_attributes(attrs, 'memberOf')
        self.objectSid = helper.get_sid(attrs, 'objectSid')
        self.objectGUID = helper.get_guid(attrs, 'objectGUID')
        self.objectGUIDHex = helper.get_guid_hex(attrs, 'objectGUID')


    @classmethod
    def get_objectclass_filter(cls, guid=None):
        if guid:
            return f"(&(objectClass=Group)(objectGUID={guid}))"
        return "(objectClass=Group)"

    @classmethod
    def get_attributes_list(cls):
        return ['*']

    @classmethod
    def get_dn_to_search(cls, ldap_config):
        return ldap_config.get_group_base_dns()

    def get_list_to_compare(self):
        return [self.distinguishedName.lower(), self.cn.lower(),
                self.sAMAccountName.lower()]

    @classmethod
    def get_defaults(cls, ldap_config, attrs):
        return ldap_config.get_group_defaults(attrs)

    @classmethod
    def _get_free_id(cls, ldap_config):
        min_id, max_id = ldap_config.get_group_min(), ldap_config.get_group_max()
        pool = set(range(min_id, max_id + 1)) # large pools not accepted: >1M

        used_ids = set(LnxGroup.objects.values_list('gid_number', flat=True))

        available_uids = pool - used_ids  # Subtract used numbers from pool
        return str(available_uids.pop()).encode('utf-8')

    @classmethod
    def _modify_ldap_entry(cls, ldap_conn, free_gid, dn):
        mod_attrs = [
            ( ldap.MOD_REPLACE, "gidNumber", free_gid)
        ]

        ldap_conn.modify_s(dn, mod_attrs)

    @classmethod
    def _create_db_entry(cls, entry_defaults, guid, free_gid):
        LnxGroup.objects.create(
            groupname=entry_defaults['sAMAccountName'].decode('utf-8'),
            gid_number=int(free_gid)
        )

    @classmethod
    @transaction.atomic
    def perform_create(cls, ldap_config, ldap_conn, dn, entry_defaults, guid):
        free_gid = cls._get_free_id(ldap_config)
        cls._create_db_entry(entry_defaults, guid, free_gid)
        cls._modify_ldap_entry(ldap_conn, free_gid, dn)

    def apply_filter(self, filter_str):
        filter_str = filter_str.lower()
        return any(filter_str in word for word in self.get_list_to_compare())


class LDAPSudoRule:

    def __init__(self, dn, attrs):
        self.helper = LDAPHelper()
        self.distinguishedName = dn
        self.name = self.helper.get_attributes(attrs, 'name')
        self.cn = self.helper.get_attributes(attrs, 'cn')
        self.description = self.helper.get_attributes(attrs, 'description')
        self.sudoCommand = self.helper.get_attributes(attrs, 'sudoCommand')
        self.sudoHost = self.helper.get_attributes(attrs, 'sudoHost')
        self.sudoOption = self.helper.get_attributes(attrs, 'sudoOption')
        self.sudoRunAsUser = self.helper.get_attributes(attrs, 'sudoRunAsUser')
        self.sudoRunAsGroup = self.helper.get_attributes(attrs, 'sudoRunAsGroup')
        self.sudoUser = self.helper.get_attributes(attrs, 'sudoUser')
        self.objectGUID = self.helper.get_guid(attrs, 'objectGUID')
        self.objectGUIDHex = self.helper.get_guid_hex(attrs, 'objectGUID')


    @classmethod
    def get_objectclass_filter(cls, guid=None):
        if guid:
            return f"(&(objectClass=sudoRole)(objectGUID={guid}))"
        return "(objectClass=sudoRole)"

    @classmethod
    def get_attributes_list(cls):
        return ['*']

    @classmethod
    def get_dn_to_search(cls, ldap_config):
        return ldap_config.get_sudo_base_dns()

    @classmethod
    def create_or_update_sudo_rule(cls, sudo_rule):
        ldap_service = LDAPObjectsService(LDAPSudoRule)
        ldap_service.create_object_by_intance(sudo_rule)
        return sudo_rule

    @classmethod
    def _create_ldap_mod_attrs(cls, sudo_rule):
        return [
            ( ldap.MOD_REPLACE, "sudoRunAs", sudo_rule.run_as_user.username.encode('utf-8')),
            ( ldap.MOD_REPLACE, "sudoRunAsUser", sudo_rule.run_as_user.username.encode('utf-8')),
            ( ldap.MOD_REPLACE, "sudoRunAsGroup", sudo_rule.run_as_group.username.encode('utf-8')),
            ( ldap.MOD_REPLACE, "sudoUser", [user.username.encode('utf-8') for user in sudo_rule.sudo_user.all()]),
            ( ldap.MOD_REPLACE, "sudoCommand", [command.full_command.encode('utf-8') for command in sudo_rule.sudo_command.all()]),
            ( ldap.MOD_REPLACE, "sudoHost", [host.hostname.encode('utf-8') for host in sudo_rule.sudo_host.all()]),
        ]

    @classmethod
    def _create_ldap_add_attrs(cls, sudo_rule):
        attrs = {}
        attrs['objectclass'] = [b'top', b'sudoRole']
        attrs['cn'] = sudo_rule.name.encode('utf-8')
        attrs['sudoRunAs'] = sudo_rule.run_as_user.username.encode('utf-8')
        attrs['sudoRunAsUser'] = sudo_rule.run_as_user.username.encode('utf-8')
        attrs['sudoRunAsGroup'] = sudo_rule.run_as_group.username.encode('utf-8')
        attrs['sudoUser'] = [user.username.encode('utf-8') for user in sudo_rule.sudo_user.all()]
        attrs['sudoCommand'] = [command.full_command.encode('utf-8') for command in sudo_rule.sudo_command.all()]
        attrs['sudoHost'] = [host.hostname.encode('utf-8') for host in sudo_rule.sudo_host.all()]
        return attrs

    @classmethod
    def _save_guid_on_entry(cls, dn, connection, sudo_rule):
        new_attrs = connection.search_s(base=dn, scope=ldap.SCOPE_BASE,
            filterstr=cls.get_objectclass_filter(), attrlist=['*'])[0][1]
        helper = LDAPHelper()
        guidhex = helper.get_guid_hex(new_attrs, 'objectGUID')
        sudo_rule.guidhex = guidhex
        sudo_rule.save()

    @classmethod
    def _create_ldap_entry(cls, connection, base_dn, attrs, sudo_rule):
        dn = f"cn={sudo_rule.name},{base_dn[0]}"
        try:
            connection.modify_s(dn, attrs)
        except ldap.NO_SUCH_OBJECT:
            attrs = cls._create_ldap_add_attrs(sudo_rule)
            ldif = modlist.addModlist(attrs)
            connection.add_s(dn, ldif)
        cls._save_guid_on_entry(dn, connection, sudo_rule)

    @classmethod
    def perform_create(cls, connection, base_dn, sudo_rule):
        attrs = cls._create_ldap_mod_attrs(sudo_rule)
        cls._create_ldap_entry(connection, base_dn, attrs, sudo_rule)
        return sudo_rule

    def apply_filter(self, filter_str):
        return (filter_str in self.name or
            any(filter_str in word for word in self.sudoCommand))
