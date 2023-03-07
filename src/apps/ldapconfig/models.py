import ldap
from django.db import models

from helpers.validators.model_validators import (validate_hostname,
    validate_host_ip, validate_dn)
from helpers.globals.choices import (LDAP_SEARCH_SCOPE,
    ONELEVEL)


class DNSHost(models.Model):

    hostname = models.CharField(max_length=253, unique=True,
        validators=[validate_host_ip]) # maximum of 253 ASCII characters

    def __str__(self):
        return self.hostname


class LDAPDn(models.Model):

    dn = models.CharField(max_length=255, unique=True,
        validators=[validate_dn])
    scope = models.CharField(
        max_length=2,
        choices=LDAP_SEARCH_SCOPE,
        default=ONELEVEL,
    )

    def __str__(self):
        return self.dn

    def get_scope(self):
        return ldap.SCOPE_ONELEVEL if self.scope == 'OL' else ldap.SCOPE_SUBTREE


class LDAPConfig(models.Model):
    domain_name = models.CharField(max_length=255, unique=True,
        validators=[validate_hostname])
    ldap_user = models.EmailField(max_length=255)
    krb_auth = models.BooleanField(default=False)
    ldap_password = models.CharField(max_length=255, blank=True,
        null=True)
    dns_hostname = models.ManyToManyField(DNSHost)
    user_dn = models.ManyToManyField(LDAPDn)
    group_dn = models.ManyToManyField(LDAPDn,
        related_name='group_ldapconfig_set')
    sudo_dn = models.ForeignKey(
        LDAPDn,
        related_name='sudo_config_set',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.domain_name

    def get_credentials(self):
        return self.ldap_user, self.ldap_password

    def get_user_base_dns(self):
        return self.user_dn.all()

    def get_group_base_dns(self):
        return self.group_dn.all()

    def get_sudo_base_dns(self):
        return [self.sudo_dn]

'''
RANGE: get list of not used numbers

start_number = 1  # Initial number in the pool
end_number = 10  # End number in the pool
used_numbers = {2, 4}  # Example set of used numbers (get IDs used from DB)

pool = set(range(start_number, end_number + 1))  # Create set of all numbers in the pool
available_numbers = pool - used_numbers  # Subtract used numbers from pool
print(available_numbers)  # Output: {1, 3, 5, 6, 7, 8, 9, 10}

'''
