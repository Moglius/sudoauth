from rest_framework import serializers

from .models import DNSHost, LDAPDn, LDAPConfig


class DNSHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DNSHost
        fields = ['pk', 'hostname']


class LDAPDnSerializer(serializers.ModelSerializer):

    class Meta:
        model = LDAPDn
        fields = ['pk', 'dn', 'scope']


class LDAPConfigSerializer(serializers.ModelSerializer):

    dns_hostname = DNSHostSerializer(many=True)
    user_dn = LDAPDnSerializer(many=True)
    group_dn = LDAPDnSerializer(many=True)

    class Meta:
        model = LDAPConfig
        fields = ['pk', 'domain_name', 'ldap_user', 'krb_auth',
            'dns_hostname', 'user_dn', 'group_dn']

    def create(self, validated_data): # POST
        return ''

    def update(self, instance, validated_data): # PATCH, PUT
        return ''
