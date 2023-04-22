from rest_framework import serializers

from apps.lnxusers.models import LnxGroup, LnxUser
from .models import (SudoRule, SudoHost, SudoCommand,
    SudoCommandRole, SudoHostGroup)


class SudoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnxUser
        fields = ['pk', 'username']


class SudoGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnxGroup
        fields = ['pk', 'groupname']


class SudoHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoHost
        fields = ['pk', 'hostname']


class SudoHostGroupListDetailSerializer(serializers.ModelSerializer):
    servers = SudoHostSerializer(many=True)

    class Meta:
        model = SudoHostGroup
        fields = '__all__'


class SudoHostGroupPutPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = SudoHostGroup
        fields = '__all__'
        extra_kwargs = {
            'name': {'read_only': True},
        }


class SudoHostGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoHostGroup
        fields = '__all__'


class SudoCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoCommand
        fields = ['pk', 'command', 'args', 'diggest', 'full_command']


class SudoCommandRoleListDetailSerializer(serializers.ModelSerializer):
    commands = SudoCommandSerializer(many=True)

    class Meta:
        model = SudoCommandRole
        fields = '__all__'


class SudoCommandRolePutPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = SudoCommandRole
        fields = '__all__'
        extra_kwargs = {
            'name': {'read_only': True},
        }


class SudoCommandRoleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SudoCommandRole
        fields = '__all__'



class SudoRuleListDetailSerializer(serializers.ModelSerializer):
    sudo_user_users = SudoUserSerializer(many=True)
    sudo_user_groups = SudoGroupSerializer(many=True)
    sudo_host_servers = SudoHostSerializer(many=True)
    sudo_host_groups = SudoHostGroupListDetailSerializer(many=True)
    sudo_command = SudoCommandSerializer(many=True)
    sudo_command_role = SudoCommandRoleListDetailSerializer(many=True)
    run_as_user = SudoUserSerializer()
    run_as_group = SudoGroupSerializer()

    class Meta:
        model = SudoRule
        fields = '__all__'


class SudoRulePutPatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = SudoRule
        fields = '__all__'
        extra_kwargs = {
            'name': {'read_only': True},
        }


class SudoRuleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SudoRule
        fields = '__all__'
