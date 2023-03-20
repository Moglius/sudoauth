from rest_framework import serializers

from .models import LnxGroup, LnxShell, LnxUser


class LnxShellSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnxShell
        fields = ['pk', 'shell']


class LnxGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = LnxGroup
        fields = ['pk', 'groupname', 'gid_number']
        extra_kwargs = {
            'groupname': {'read_only': True},
        }


class LnxUserListDetailSerializer(serializers.ModelSerializer):

    primary_group = LnxGroupSerializer()
    login_shell = LnxShellSerializer()

    class Meta:
        model = LnxUser
        fields = ['pk', 'username', 'uid_number', 'primary_group',
            'login_shell', 'home_dir', 'gecos']


class LnxUserPutPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = LnxUser
        fields = ['username', 'uid_number', 'primary_group',
            'login_shell', 'home_dir', 'gecos']
        extra_kwargs = {
            'username': {'read_only': True},
        }
