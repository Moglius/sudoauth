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

    def __str__(self):
        return self.domain_name
    
    def get_credentials(self):
        return self.ldap_user, self.ldap_password
