import ldap
from django.http import Http404

from apps.ldapconfig.models import LDAPConfig
from .discovery import DNSService


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
            attrlist=self.attrlist,
            serverctrls=[ctrl],
            timeout=50
        )

        _r_type, res, _r_mid, srv_crtls = self.connection.result3(
            msgid,
            timeout=50,
        )
        return res, srv_crtls

    def _perform_search(self, res, search_dname):

        for base_dn in search_dname:
            pk = base_dn.pk
            res[pk]['res'], res[pk]['ctrl'] = self._ldap_search(base_dn, res[pk]['cookie'])

        return res

    def _search_on_dn(self, dn, filterstr):
        try:
            return self.connection.search_s(
                base=dn.dn,
                scope=dn.get_scope(),
                filterstr=filterstr,
                attrlist=['*'])
        except Exception as exc:
            raise Http404 from exc

    def _ldap_search_by_guid(self, base_dn, guid):
        guid = ''.join([f"\\{guid[i:i+2]}" for i in range(0, len(guid), 2)])
        filterstr = self.return_class.get_objectclass_filter(guid)
        for dn in base_dn:
            result = self._search_on_dn(dn, filterstr)
            if result:
                break
        if result:
            return result[0]
        raise Http404

    def _perform_search_by_guid(self, search_dname, guid):
        result = self._ldap_search_by_guid(search_dname, guid)
        return result

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
        keep_dn_search = []
        remove_dn_search = []
        for key, ldap_search in search_res.items():
            page_crtl = self._get_page_control(ldap_search['ctrl'])
            if page_crtl.cookie:
                keep_dn_search.append(key)
                ldap_search['cookie'].cookie = page_crtl.cookie
            else:
                remove_dn_search.append(key)

        for key in remove_dn_search:
            del search_res[key]
        return keep_dn_search

    def _get_dn_ramaining_dn(self, search_dname, keep_dn_search):

        new_search_dname = []
        for search_dn in search_dname:
            if search_dn.pk in keep_dn_search:
                new_search_dname.append(search_dn)

        return new_search_dname

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

    def get_objects(self):

        search_dname = list(self._get_dn_to_search())
        search_res = self._create_working_dictionary(search_dname)

        while True:
            self._perform_search(search_res, search_dname)

            for search in search_res.values():
                for d_name, attrs in search['res']:
                    print(attrs)
                    if d_name is not None:
                        yield self._create_return_object(d_name, attrs)

            if self._more_ldap_pages(search_res):
                keep_dn_search = self._set_cookie(search_res)
                search_dname = self._get_dn_ramaining_dn(search_dname, keep_dn_search)
            else:
                break

    def get_object(self, guid):

        search_dname = self._get_dn_to_search()
        dn, attrs = self._perform_search_by_guid(search_dname, guid)
        return self._create_return_object(dn, attrs)

    def create_object_by_guid(self, guid):

        search_dname = self._get_dn_to_search()
        dn, attrs = self._perform_search_by_guid(search_dname, guid)
        entry_defaults = self.return_class.get_defaults(self.ldap_config, attrs)
        self.return_class.perform_create(self.ldap_config, self.connection,
            dn, entry_defaults, guid)
        return self._create_return_object(dn, attrs)

    def update_by_instance(self, instance):
        search_dname = self._get_dn_to_search()
        dn, attrs = self._perform_search_by_guid(search_dname, instance.get_guid())
        self.return_class.perform_update(self.connection, dn, instance)

    def create_object_by_intance(self, instance):
        base_dn = self._get_dn_to_search()
        self.return_class.perform_create(self.connection, base_dn, instance)
        return instance

    def clear_by_instance(self, instance):
        ldap_entry = self.get_object(instance.guidhex)
        self.return_class.perform_clear(self.connection, ldap_entry)

    def destroy_by_instance(self, instance):
        ldap_entry = self.get_object(instance.guidhex)
        self.connection.delete_s(ldap_entry.distinguishedName)
