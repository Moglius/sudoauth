from rest_framework import serializers

from .models import (
    LnxGroup,
    LnxShell
)


class LnxShellSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnxShell
        fields = ['shell']


class LnxGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = LnxGroup
        fields = ['groupname', 'gid_number']
