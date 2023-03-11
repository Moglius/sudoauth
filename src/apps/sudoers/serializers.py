from rest_framework import serializers

from .models import (SudoRule, SudoUser,
    SudoHost, SudoCommand)


class SudoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoUser
        fields = ['pk', 'username']
        extra_kwargs = {
            'username': {'validators': []},
        }


class SudoHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoHost
        fields = ['pk', 'hostname']
        extra_kwargs = {
            'hostname': {'validators': []},
        }


class SudoCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoCommand
        fields = ['pk', 'command', 'args', 'diggest']
        extra_kwargs = {
            'command': {'validators': []},
        }


class SudoRuleSerializer(serializers.ModelSerializer):
    sudo_user = SudoUserSerializer(many=True)
    sudo_host = SudoHostSerializer(many=True)
    sudo_command = SudoCommandSerializer(many=True)
    run_as_user = SudoUserSerializer()
    run_as_group = SudoUserSerializer()

    class Meta:
        model = SudoRule
        fields = ['pk', 'name', 'sudo_user', 'sudo_host',
            'sudo_command', 'run_as_user', 'run_as_group']

    def _create_sudo_rule(self, validated_data):
        run_as_user = SudoUser.get_instance(validated_data.pop('run_as_user'))
        run_as_group = SudoUser.get_instance(validated_data.pop('run_as_group'))
        name = validated_data.pop('name')
        return SudoRule.objects.create(
            name=name,
            run_as_group=run_as_group,
            run_as_user=run_as_user
        )

    def _add_fields_m2m(self, validated_data, sudo_rule):
        sudo_users = SudoUser.get_instances(validated_data.pop('sudo_user'))
        sudo_hosts = SudoHost.get_instances(validated_data.pop('sudo_host'))
        sudo_commands = SudoCommand.get_instances(validated_data.pop('sudo_command'))
        sudo_rule.sudo_user.add(*sudo_users)
        sudo_rule.sudo_host.add(*sudo_hosts)
        sudo_rule.sudo_command.add(*sudo_commands)
        return sudo_rule

    def create(self, validated_data): # POST
        sudo_rule = self._create_sudo_rule(validated_data)
        return self._add_fields_m2m(validated_data, sudo_rule)

    def update(self, instance, validated_data): # PATCH, PUT
        print(validated_data)
        print(instance)
        return ''
