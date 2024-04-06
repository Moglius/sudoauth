from apps.lnxusers.models import LnxGroup, LnxUser
from rest_framework import serializers

from .models import SudoCommand, SudoCommandRole, SudoHost, SudoHostGroup, SudoRule


class SudoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnxUser
        fields = ["pk", "username"]


class SudoGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = LnxGroup
        fields = ["pk", "groupname"]


class SudoHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoHost
        fields = ["pk", "hostname"]


class SudoHostGroupPutPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoHostGroup
        fields = "__all__"
        extra_kwargs = {
            "name": {"read_only": True},
        }


class SudoHostGroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoHostGroup
        fields = "__all__"


class SudoHostGroupListDetailSerializer(serializers.ModelSerializer):
    servers = SudoHostSerializer(many=True)
    nested = SudoHostGroupCreateSerializer(many=True)

    class Meta:
        model = SudoHostGroup
        fields = "__all__"


class SudoCommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoCommand
        fields = ["pk", "command", "args", "diggest", "full_command"]


class SudoCommandRolePutPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoCommandRole
        fields = "__all__"
        extra_kwargs = {
            "name": {"read_only": True},
        }


class SudoCommandRoleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoCommandRole
        fields = "__all__"


class SudoCommandRoleListDetailSerializer(serializers.ModelSerializer):
    commands = SudoCommandSerializer(many=True)

    class Meta:
        model = SudoCommandRole
        fields = "__all__"


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
        fields = "__all__"


class SudoRulePutPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoRule
        fields = "__all__"
        extra_kwargs = {
            "name": {"read_only": True},
        }

    def validate(self, attrs):
        if len(attrs["sudo_user_users"]) == 0 and len(attrs["sudo_user_groups"]) == 0:
            raise serializers.ValidationError(
                "sudo_user_users/sudo_user_groups fields cannot be both null/blank."
            )

        return super().validate(attrs)


class SudoRuleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoRule
        fields = "__all__"
