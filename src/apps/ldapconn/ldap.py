import ldap

from .models import LDAPUser
from apps.ldapconfig.models import LDAPConfig
from .discovery import DNSService


LDAP_SERVER = 'ldap://192.168.0.44'
BASE_DN = 'dc=localdomain,dc=com'  # base dn to search in
LDAP_LOGIN = 'syncuser@localdomain.com'
LDAP_PASSWORD = "Vyq59[Tc/?6k4bT2]%aE"


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

    mod_attrs = [( ldap.MOD_REPLACE, "gidNumber", gidnumber.encode('utf-8'))]

    connect.modify_s(dn, mod_attrs)


class LDAPObjectsService():

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(LDAPObjectsService, cls).__new__(cls)
        return cls.instance

    def _get_ldap_servers(self):
        dns_service = DNSService()
        return dns_service.get_ldap_servers()

    def _get_credentials(self):
        ldap_config = LDAPConfig.objects.first()
        return ldap_config.get_credentials()

    def _init_connection(self):
        server = self._get_ldap_servers()[0]
        connect = ldap.initialize(server)
        connect.set_option(ldap.OPT_REFERRALS, 0)
        user, passwd = self._get_credentials()
        connect.simple_bind_s(user, passwd)
        return connect

    def __init__(self):
        self.connection = self._init_connection()
        self.ldap_control = ldap.controls.SimplePagedResultsControl(
            criticality=False,
            size=1000,
            cookie='',
        )

    def _perform_search(self):

        BASE_DN = 'CN=Users,DC=localdomain,DC=com'
        OBJECT_TO_SEARCH = "(&(objectClass=Person)(userPrincipalName=*))"
        ATTRIBUTES_TO_SEARCH = ['gidNumber', 'userPrincipalName']

        msgid = self.connection.search_ext(
            base=BASE_DN,
            scope=ldap.SCOPE_ONELEVEL,
            filterstr=OBJECT_TO_SEARCH,
            attrlist=ATTRIBUTES_TO_SEARCH,
            serverctrls=[self.ldap_control],
            timeout=5
        )

        _res_type, results, _res_msgid, server_controls = self.connection.result3(
            msgid,
            timeout=5,
        )

        return results, server_controls

    def _get_page_control(self, server_controls):
        output = None
        for ctrl in server_controls:
            if ctrl.controlType == ldap.CONTROL_PAGEDRESULTS:
                output = ctrl
        return output

    def _create_return_object(self, d_name, attrs):
        return LDAPUser(d_name, attrs['userPrincipalName'][0].decode('utf-8'))

    def get_objects(self):

        while True:

            results, server_controls = self._perform_search()

            for d_name, attrs in results:
                if d_name is not None:
                    yield self._create_return_object(d_name, attrs)

            page_control = self._get_page_control(server_controls)
            if page_control.cookie:
                self.ldap_control.cookie = page_control.cookie
            else:
                break
