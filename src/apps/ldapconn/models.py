import struct, uuid, binascii


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
    def get_objectclass_filter(cls):
        return "(&(objectClass=Person)(userPrincipalName=*))"

    @classmethod
    def get_attributes_list(cls):
        return ['*']

    @classmethod
    def get_dn_to_search(cls, ldap_config):
        return ldap_config.get_user_base_dns()


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
    def get_objectclass_filter(cls):
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

    def apply_filter(self, filter_str):
        filter_str = filter_str.lower()
        return any(filter_str in word for word in self.get_list_to_compare())


class LDAPSudoRule:

    def __init__(self, dn, attrs):
        helper = LDAPHelper()
        self.distinguishedName = dn
        self.name = helper.get_attributes(attrs, 'name')
        self.cn = helper.get_attributes(attrs, 'cn')
        self.description = helper.get_attributes(attrs, 'description')
        self.sudoCommand = helper.get_attributes(attrs, 'sudoCommand')
        self.sudoHost = helper.get_attributes(attrs, 'sudoHost')
        self.sudoOption = helper.get_attributes(attrs, 'sudoOption')
        self.sudoRunAsUser = helper.get_attributes(attrs, 'sudoRunAsUser')
        self.sudoRunAsGroup = helper.get_attributes(attrs, 'sudoRunAsGroup')
        self.sudoUser = helper.get_attributes(attrs, 'sudoUser')
        self.objectGUID = helper.get_guid(attrs, 'objectGUID')
        self.objectGUIDHex = helper.get_guid_hex(attrs, 'objectGUID')


    @classmethod
    def get_objectclass_filter(cls):
        return "(objectClass=sudoRole)"

    @classmethod
    def get_attributes_list(cls):
        return ['*']

    @classmethod
    def get_dn_to_search(cls, ldap_config):
        return ldap_config.get_sudo_base_dns()

    def apply_filter(self, filter_str):
        return (filter_str in self.name or
            any(filter_str in word for word in self.sudoCommand))
