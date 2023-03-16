from rest_framework import serializers

from apps.ldapconn.models import LDAPSudoRule
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
        fields = ['pk', 'command', 'args', 'diggest', 'full_command']
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

    def _update_sudo_rule(self, sudo_rule, validated_data):
        if 'run_as_user' in validated_data:
            sudo_rule.run_as_user = SudoUser.get_instance(
                validated_data.pop('run_as_user'))
        if 'run_as_group' in validated_data:
            sudo_rule.run_as_group = SudoUser.get_instance(
                validated_data.pop('run_as_group'))
        return sudo_rule

    def _assign_m2m_fields(self, key, validated_data, cur_class, sudo_rule_m2m):
        if key in validated_data:
            items = cur_class.get_instances(
                validated_data.pop(key))
            sudo_rule_m2m.clear()
            sudo_rule_m2m.add(*items)

    def _add_m2m_fields(self, sudo_rule, validated_data):
        self._assign_m2m_fields('sudo_user', validated_data,
                                SudoUser, sudo_rule.sudo_user)
        self._assign_m2m_fields('sudo_host', validated_data,
                                SudoHost, sudo_rule.sudo_host)
        self._assign_m2m_fields('sudo_command', validated_data,
                                SudoCommand, sudo_rule.sudo_command)
        return sudo_rule

    def create(self, validated_data): # POST
        sudo_rule = self._create_sudo_rule(validated_data)
        sudo_rule = self._add_m2m_fields(sudo_rule, validated_data)
        sudo_rule.save()
        LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return sudo_rule

    def update(self, instance, validated_data): # PATCH (partial), PUT
        sudo_rule = self._update_sudo_rule(instance, validated_data)
        sudo_rule = self._add_m2m_fields(sudo_rule, validated_data)
        sudo_rule.save()
        LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return sudo_rule
