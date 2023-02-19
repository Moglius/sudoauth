from rest_framework import serializers

from .models import (
    SudoRule,
    SudoUser,
    SudoHost,
    SudoCommand,
)


class SudoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoUser
        fields = ['username']


class SudoHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoHost
        fields = ['hostname']


class SudoCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoCommand
        fields = ['command', 'diggest']


class SudoRuleSerializer(serializers.ModelSerializer):
    sudo_user = SudoUserSerializer(many=True)
    sudo_host = SudoHostSerializer(many=True)
    sudo_command = SudoCommandSerializer(many=True)
    run_as_user = SudoUserSerializer()
    run_as_group = SudoUserSerializer()

    class Meta:
        model = SudoRule
        fields = ['name', 'sudo_user', 'sudo_host',
            'sudo_command', 'run_as_user', 'run_as_group']

    def create(self, validated_data): # POST
        sudo_users = validated_data.pop('sudo_user')
        print(sudo_users)
        return ''

    def update(self, instance, validated_data): # PATCH, PUT
        print(validated_data)
        print(instance)
        return ''
