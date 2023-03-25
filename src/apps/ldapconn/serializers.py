from rest_framework import serializers


class LDAPUserSerializer(serializers.Serializer):
    distinguishedName = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    cn = serializers.CharField(max_length=255)
    sAMAccountName = serializers.CharField(max_length=255)
    givenName = serializers.CharField(max_length=255)
    sn = serializers.CharField(max_length=255)
    objectSid = serializers.CharField(max_length=255)
    objectGUID = serializers.CharField(max_length=255)
    objectGUIDHex = serializers.CharField(max_length=255)


class LDAPGroupSerializer(serializers.Serializer):
    distinguishedName = serializers.CharField(max_length=255)
    sAMAccountName = serializers.CharField(max_length=255)
    cn = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    member = serializers.ListField(
        child=serializers.CharField(max_length=255)
    )
    memberOf = serializers.ListField(
        child=serializers.CharField(max_length=255)
    )
    objectSid = serializers.CharField(max_length=255)
    objectGUID = serializers.CharField(max_length=255)
    objectGUIDHex = serializers.CharField(max_length=255)


class LDAPSudoRuleSerializer(serializers.Serializer):
    distinguishedName = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    cn = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    sudoCommand = serializers.ListField(
        child=serializers.CharField(max_length=255)
    )
    sudoHost = serializers.ListField(
        child=serializers.CharField(max_length=255)
    )
    sudoOption = serializers.ListField(
        child=serializers.CharField(max_length=255)
    )
    sudoRunAsUser = serializers.CharField(max_length=255)
    sudoRunAsGroup = serializers.CharField(max_length=255)
    sudoUser = serializers.ListField(
        child=serializers.CharField(max_length=255)
    )
    objectGUID = serializers.CharField(max_length=255)
    objectGUIDHex = serializers.CharField(max_length=255)


class LDAPUserGroupCreationSerializer(serializers.Serializer):
    objectGUIDHex = serializers.CharField(max_length=255)

    def get_guid(self):
        return self.data['objectGUIDHex']
