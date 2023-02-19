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


class LnxUserSerializer(serializers.ModelSerializer):

    primary_group = LnxGroupSerializer()
    login_shell = LnxShellSerializer()

    class Meta:
        model = LnxUser
        fields = ['pk', 'username', 'uid_number', 'primary_group',
            'login_shell', 'home_dir', 'gecos']

    def create(self, validated_data): # POST
        sudo_users = validated_data.pop('sudo_user')
        print(sudo_users)
        return ''

    def update(self, instance, validated_data): # PATCH, PUT
        print(validated_data)
        print(instance)
        return ''
