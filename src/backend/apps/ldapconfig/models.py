import ldap
from apps.lnxusers.models import LnxGroup, LnxShell
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from helpers.globals.choices import LDAP_SEARCH_SCOPE, ONELEVEL
from helpers.validators.model_validators import (
    validate_dn,
    validate_host_ip,
    validate_hostname,
)


class DNSHost(models.Model):
    hostname = models.CharField(
        max_length=253, unique=True, validators=[validate_host_ip]
    )  # maximum of 253 ASCII characters

    def __str__(self):
        return self.hostname


class LDAPDn(models.Model):
    dn = models.CharField(max_length=255, unique=True, validators=[validate_dn])
    scope = models.CharField(
        max_length=2,
        choices=LDAP_SEARCH_SCOPE,
        default=ONELEVEL,
    )

    def __str__(self):
        return self.dn

    def get_scope(self):
        return ldap.SCOPE_ONELEVEL if self.scope == "OL" else ldap.SCOPE_SUBTREE


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
    domain_name = models.CharField(max_length=255, unique=True, validators=[validate_hostname])
    ldap_user = models.EmailField(max_length=255)
    krb_auth = models.BooleanField(default=False)
    ldap_password = models.CharField(max_length=255, blank=True, null=True)
    dns_hostname = models.ManyToManyField(DNSHost)
    user_dn = models.ManyToManyField(LDAPDn)
    group_dn = models.ManyToManyField(LDAPDn, related_name="group_ldapconfig_set")
    sudo_dn = models.ForeignKey(LDAPDn, related_name="sudo_config_set", on_delete=models.CASCADE)
    nis_netgroup_dn = models.ForeignKey(
        LDAPDn, related_name="nis_netgroup_config_set", on_delete=models.CASCADE
    )
    users_pool = models.ForeignKey(
        PoolRange, default=1, related_name="config_user_pool_set", on_delete=models.CASCADE
    )
    groups_pool = models.ForeignKey(
        PoolRange, default=1, related_name="config_group_pool_set", on_delete=models.CASCADE
    )
    default_group = models.ForeignKey(
        LnxGroup, default=1, related_name="default_group_set", on_delete=models.CASCADE
    )
    default_shell = models.ForeignKey(
        LnxShell, default=1, related_name="default_shell_set", on_delete=models.CASCADE
    )

    @classmethod
    def get_default_group(cls):
        ldap_config = LDAPConfig.objects.first()
        return ldap_config.default_group

    @classmethod
    def get_default_shell(cls):
        ldap_config = LDAPConfig.objects.first()
        return ldap_config.default_shell

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

    def get_nis_netgroup_base_dns(self):
        return [self.nis_netgroup_dn]

    def get_user_min(self):
        return self.users_pool.pool_min

    def get_user_max(self):
        return self.users_pool.pool_max

    def get_group_min(self):
        return self.groups_pool.pool_min

    def get_group_max(self):
        return self.groups_pool.pool_max

    def get_user_defaults(self, attrs):
        username = attrs["sAMAccountName"][0].decode("utf-8")
        return {
            "homeDirectory": f"/home/{username}".encode("utf-8"),
            "gidNumber": self.default_group.get_gid_number().encode("utf-8"),
            "loginShell": self.default_shell.get_shell_name().encode("utf-8"),
            "gecos": attrs["displayName"][0],
            "uid": attrs["sAMAccountName"][0],
        }

    def get_group_defaults(self, attrs):
        return {"sAMAccountName": attrs["sAMAccountName"][0]}
