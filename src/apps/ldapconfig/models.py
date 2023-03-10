import ldap
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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


class PoolRange(models.Model):
    pool_min = models.PositiveBigIntegerField(
        default=50000,
        validators=[MinValueValidator(1000), MaxValueValidator(4294967295)],
    )
    pool_max = models.PositiveBigIntegerField(
        default=60000,
        validators=[MinValueValidator(1000), MaxValueValidator(4294967295)],
    )

    def __str__(self):
        return f"{self.pool_min}-{self.pool_max}"


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
    users_pool = models.ForeignKey(
        PoolRange,
        default=1,
        related_name='config_user_pool_set',
        on_delete=models.CASCADE
    )
    groups_pool = models.ForeignKey(
        PoolRange,
        default=1,
        related_name='config_group_pool_set',
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

    def get_user_min(self):
        return self.users_pool.pool_min
    
    def get_user_max(self):
        return self.users_pool.pool_max
    
    def get_user_defaults(self):
        return {
            "primary_group": 1231232, # TODO: get this from this model
            "shell": '/bin/bash' # TODO: get this from this model
        }
