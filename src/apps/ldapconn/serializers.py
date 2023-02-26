from rest_framework import serializers


class LDAPUserSerializer(serializers.Serializer):
    distinguishedName = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    cn = serializers.CharField(max_length=255)
    sAMAccountName = serializers.CharField(max_length=255)
    givenName = serializers.CharField(max_length=255)
    sn = serializers.CharField(max_length=255)


class LDAPGroupSerializer(serializers.Serializer):
    distinguishedName = serializers.CharField(max_length=255)
    sAMAccountName = serializers.CharField(max_length=255)
    cn = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    member = serializers.CharField(max_length=255)
    memberOf = serializers.CharField(max_length=255)
