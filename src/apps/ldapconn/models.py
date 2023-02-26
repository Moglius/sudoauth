

class LDAPUser:

    def __init__(self, dn, attrs):
        self.distinguishedName = dn
        self.name = attrs['name'][0].decode('utf-8')
        self.userPrincipalName = attrs['userPrincipalName'][0].decode('utf-8')
        self.cn = attrs['cn'][0].decode('utf-8')
        self.sAMAccountName = attrs['sAMAccountName'][0].decode('utf-8')
        self.givenName = attrs['givenName'][0].decode('utf-8')
        self.sn = attrs['sn'][0].decode('utf-8')

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

    def _get_attributes(self, attrs, key):
        return attrs[key][0].decode('utf-8') if key in attrs else 'N/A'

    def __init__(self, dn, attrs):
        self.distinguishedName = dn
        self.sAMAccountName = attrs['sAMAccountName'][0].decode('utf-8')
        self.cn = attrs['cn'][0].decode('utf-8')
        self.description = attrs['description'][0].decode('utf-8')
        self.member = self._get_attributes(attrs, 'member')
        self.memberOf = self._get_attributes(attrs, 'memberOf')


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
