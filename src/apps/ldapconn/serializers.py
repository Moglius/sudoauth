from rest_framework import serializers


class LDAPUserSerializer(serializers.Serializer):
    dn = serializers.CharField(max_length=255)
    upn = serializers.CharField(max_length=255)
