from apps.lnxusers.serializers import LnxGroupSerializer, LnxShellSerializer
from rest_framework import serializers

from .models import DNSHost, LDAPConfig, LDAPDn, PoolRange


class DNSHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DNSHost
        fields = ["pk", "hostname"]


class LDAPDnSerializer(serializers.ModelSerializer):
    class Meta:
        model = LDAPDn
        fields = ["pk", "dn", "scope"]


class PoolRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolRange
        fields = ["pk", "pool_min", "pool_max"]


class LDAPConfigSerializer(serializers.ModelSerializer):
    dns_hostname = DNSHostSerializer(many=True)
    user_dn = LDAPDnSerializer(many=True)
    group_dn = LDAPDnSerializer(many=True)
    sudo_dn = LDAPDnSerializer()
    users_pool = PoolRangeSerializer()
    groups_pool = PoolRangeSerializer()
    default_group = LnxGroupSerializer()
    default_shell = LnxShellSerializer()

    class Meta:
        model = LDAPConfig
        exclude = ("ldap_password",)

    def create(self, validated_data):  # POST
        return ""

    def update(self, instance, validated_data):  # PATCH, PUT
        return ""
