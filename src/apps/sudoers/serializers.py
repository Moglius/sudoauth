from rest_framework import serializers

from .models import (SudoRule, SudoUser,
    SudoHost, SudoCommand)


class SudoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoUser
        fields = ['pk', 'username']


class SudoHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoHost
        fields = ['pk', 'hostname']


class SudoCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoCommand
        fields = ['pk', 'command', 'args', 'diggest', 'full_command']


class SudoRuleListDetailSerializer(serializers.ModelSerializer):
    sudo_user = SudoUserSerializer(many=True)
    sudo_host = SudoHostSerializer(many=True)
    sudo_command = SudoCommandSerializer(many=True)
    run_as_user = SudoUserSerializer()
    run_as_group = SudoUserSerializer()

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
        #fields = ['pk', 'name', 'sudo_user', 'sudo_host',
        #    'sudo_command', 'run_as_user', 'run_as_group']
        fields = '__all__'
