import binascii
import ldap
import ldap.modlist as modlist
from django.http import Http404

from apps.ldapconfig.models import LDAPConfig
from .discovery import DNSService


# Autofs:
# https://ovalousek.wordpress.com/2015/08/03/autofs/


LDAP_SERVER = 'ldap://192.168.0.44'
BASE_DN = 'dc=localdomain,dc=com'  # base dn to search in
LDAP_LOGIN = 'syncuser@localdomain.com'
LDAP_PASSWORD = "Vyq59[Tc/?6k4bT2]%aE"

def guid2hexstring(val):
    s = ['\\%02X' % ord(x) for x in val]
    return ''.join(s)


def search_by_sid():

    OBJECT_TO_SEARCH = "objectSid=S-1-5-21-3541430928-2051711210-1391384369-1108"
    ATTRIBUTES_TO_SEARCH = ['*']

    connect = ldap.initialize(LDAP_SERVER)
    connect.set_option(ldap.OPT_REFERRALS, 0)  # to search the object and all its descendants
    connect.simple_bind_s(LDAP_LOGIN, LDAP_PASSWORD)
    result = connect.search_s(BASE_DN, ldap.SCOPE_SUBTREE, OBJECT_TO_SEARCH, ATTRIBUTES_TO_SEARCH)

    guid = result[0][1]['objectGUID'][0]

    guid = binascii.hexlify(guid).decode('utf-8')
    print(guid)

    guid = ''.join(['\\%s' % guid[i:i+2] for i in range(0, len(guid), 2)])
    print(guid)

    OBJECT_TO_SEARCH = f"(objectGUID={guid})"
    ATTRIBUTES_TO_SEARCH = ['*']

    connect = ldap.initialize(LDAP_SERVER)
    connect.set_option(ldap.OPT_REFERRALS, 0)  # to search the object and all its descendants
    connect.simple_bind_s(LDAP_LOGIN, LDAP_PASSWORD)
    result2 = connect.search_s(BASE_DN, ldap.SCOPE_SUBTREE, OBJECT_TO_SEARCH, ATTRIBUTES_TO_SEARCH)
    print('-------------------')
    print(result2[0])
    print('-------------------')

def search_by_guid():

    OBJECT_TO_SEARCH = "(objectGUID=1556461e48de4821a4ba62b0df60363a)"
    ATTRIBUTES_TO_SEARCH = ['*']

    connect = ldap.initialize(LDAP_SERVER)
    connect.set_option(ldap.OPT_REFERRALS, 0)  # to search the object and all its descendants
    connect.simple_bind_s(LDAP_LOGIN, LDAP_PASSWORD)
    result = connect.search_s(BASE_DN, ldap.SCOPE_SUBTREE, OBJECT_TO_SEARCH, ATTRIBUTES_TO_SEARCH)

    print(result[0])


def modify_user():

    OBJECT_TO_SEARCH = 'userPrincipalName=syncuser@localdomain.com'
    ATTRIBUTES_TO_SEARCH = ['gidNumber']

    connect = ldap.initialize(LDAP_SERVER)
    connect.set_option(ldap.OPT_REFERRALS, 0)  # to search the object and all its descendants
    connect.simple_bind_s(LDAP_LOGIN, LDAP_PASSWORD)
    result = connect.search_s(BASE_DN, ldap.SCOPE_SUBTREE, OBJECT_TO_SEARCH, ATTRIBUTES_TO_SEARCH)

    print(result[0])
    gidnumber = str(int(result[0][1]['gidNumber'][0].decode('utf-8')) + 1)

    dn = result[0][0]

    mod_attrs = [( ldap.MOD_REPLACE, "gidNumber", gidnumber.encode('utf-8')),
                 ( ldap.MOD_REPLACE, "uidNumber", gidnumber.encode('utf-8')),
                 ( ldap.MOD_REPLACE, "gecos", b'syncuser'),
                 ( ldap.MOD_REPLACE, "homeDirectory", b'/home/syncuser'),
                 ( ldap.MOD_REPLACE, "loginShell", b'/usr/bin/bash')]

    connect.modify_s(dn, mod_attrs)

def create_sudo_rule():

    dn = "cn=RITM23123124,ou=sudo,dc=localdomain,dc=com"

    attrs = {}
    attrs['cn'] = b'RITM23123124'
    attrs['objectclass'] = [
        b'top',
        b'sudoRole',
    ]
    attrs['sudoOption'] = b'!authenticate'
    attrs['sudoRunAs'] = b'root'
    attrs['sudoRunAsGroup'] = b'root'
    attrs['sudoRunAsUser'] = b'root'

    attrs['sudoUser'] = [b'syncuser', b'%syncgroup']
    attrs['sudoCommand'] = [b'/bin/dmidecode -q 1', b'/bin/tail -f /var/log/secure']
    attrs['sudoHost'] = [b'host1.localdomain.com', b'host2.localdomain.com']

    connect = ldap.initialize(LDAP_SERVER)
    connect.set_option(ldap.OPT_REFERRALS, 0)  # to search the object and all its descendants
    connect.simple_bind_s(LDAP_LOGIN, LDAP_PASSWORD)

    ldif = modlist.addModlist(attrs)
    connect.add_s(dn, ldif)
    connect.unbind_s()


class LDAPObjectsService():

    def __new__(cls, ldap_obj_class):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LDAPObjectsService, cls).__new__(cls)
        return cls.instance

    def _get_ldap_servers(self):
        dns_service = DNSService()
        return dns_service.get_ldap_servers()

    def _get_credentials(self):
        return self.ldap_config.get_credentials()

    def _init_connection(self):
        server = self._get_ldap_servers()[0]
        connect = ldap.initialize(server)
        connect.set_option(ldap.OPT_REFERRALS, 0)
        user, passwd = self._get_credentials()
        connect.simple_bind_s(user, passwd)
        return connect

    def __init__(self, ldap_obj_class):
        self.ldap_config = LDAPConfig.objects.first()
        self.connection = self._init_connection()
        self.filterstr = ldap_obj_class.get_objectclass_filter()
        self.attrlist = ldap_obj_class.get_attributes_list()
        self.return_class = ldap_obj_class

    def _get_dn_to_search(self):
        return self.return_class.get_dn_to_search(self.ldap_config)

    def _ldap_search(self, base_dn, ctrl):

        msgid = self.connection.search_ext(
            base=base_dn.dn,
            scope=base_dn.get_scope(),
            filterstr=self.filterstr,
            attrlist=['*'],
            serverctrls=[ctrl],
            timeout=5
        )

        _r_type, res, _r_mid, srv_crtls = self.connection.result3(
            msgid,
            timeout=5,
        )
        return res, srv_crtls

    def _perform_search(self, res, search_dname):

        for base_dn in search_dname:
            pk = base_dn.pk
            res[pk]['res'], res[pk]['ctrl'] = self._ldap_search(base_dn, res[pk]['cookie'])

        return res

    def _ldap_search_by_guid(self, base_dn, guid):
        guid = ''.join([f"\\{guid[i:i+2]}" for i in range(0, len(guid), 2)])

        for dn in base_dn:
            try:
                result = self.connection.search_s(dn.dn, dn.get_scope(),
                    f"objectGUID={guid}", ['*'])
            except Exception as exc:
                raise Http404 from exc
            if result:
                break

        return result

    def _perform_search_by_guid(self, search_dname, guid):
        result = self._ldap_search_by_guid(search_dname, guid)
        return result[0]

    def _get_page_control(self, server_controls):
        output = None
        for ctrl in server_controls:
            if ctrl.controlType == ldap.CONTROL_PAGEDRESULTS:
                output = ctrl
        return output

    def _create_return_object(self, d_name, attrs):
        return self.return_class(d_name, attrs)

    def _more_ldap_pages(self, search_res):
        for ldap_search in search_res.values():
            page_crtl = self._get_page_control(ldap_search['ctrl'])
            if page_crtl.cookie: return True
        return False

    def _set_cookie(self, search_res):
        for ldap_search in search_res:
            page_crtl = self._get_page_control(ldap_search['ctrl'])
            if page_crtl.cookie: 
                ldap_search['cookie'].cookie = page_crtl.cookie

    def _create_working_dictionary(self, search_dname):

        res = {}
        for base_dn in search_dname:
            pk = base_dn.pk
            res[pk] = {}
            res[pk]['cookie'] = ldap.controls.SimplePagedResultsControl(
                criticality=False,
                size=1000,
                cookie='',
            )
            res[pk]['res'], res[pk]['ctrl'] = None, None
        return res

    def _perform_create(self, dn, entry_defaults, guid):
        ''' CODE RUN in a Transaction
        TODO: get next number from pool, assign defaults
            modify ldap entry, create DB entry with guid
        '''
        return

    def get_objects(self):

        search_dname = self._get_dn_to_search()
        search_res = self._create_working_dictionary(search_dname)

        while True:

            self._perform_search(search_res, search_dname)

            for search in search_res.values():
                for d_name, attrs in search['res']:
                    if d_name is not None:
                        yield self._create_return_object(d_name, attrs)

            if self._more_ldap_pages(search_res):
                self._set_cookie(search_res)
            else:
                break

    def get_object(self, guid):

        search_dname = self._get_dn_to_search()
        result = self._perform_search_by_guid(search_dname, guid)
        return self._create_return_object(result[0], result[1])
    
    def create_object(self, guid):

        search_dname = self._get_dn_to_search()
        dn, attrs = self._perform_search_by_guid(search_dname, guid)
        entry_defaults = self.return_class.get_defaults(self.ldap_config)
        self._perform_create(dn, entry_defaults, guid)
        return 'user'
