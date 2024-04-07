import dns.resolver
from apps.ldapconfig.models import LDAPConfig


class DNSService:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(DNSService, cls).__new__(cls)
        return cls.instance

    def get_dns_servers(self):
        ldap_config = LDAPConfig.objects.first()
        dns_servers = ldap_config.dns_hostname.values_list("hostname", flat=True)
        domain = ldap_config.domain_name
        return dns_servers, domain

    def extract_ldap_servers(self, srv_records):
        ldap_servers = []
        for srv in srv_records:
            srv_name = str(srv.target).rstrip(".")
            ldap_servers.append(f"ldap://{srv_name}")

        return ldap_servers

    def get_ldap_list(self, dns_servers, domain):
        dns_resolver = dns.resolver.Resolver()

        ldap_servers = []

        for dns_server in dns_servers:
            dns_resolver.nameservers = [dns_server]
            srv_records = dns_resolver.query(f"_ldap._tcp.{domain}", "SRV")
            if len(srv_records) > 0:
                ldap_servers = self.extract_ldap_servers(srv_records)
                break

        return ldap_servers

    def get_ldap_servers(self):
        dns_servers, domain = self.get_dns_servers()
        return self.get_ldap_list(dns_servers, domain)
