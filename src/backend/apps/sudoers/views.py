from apps.ldapconn.ldap import LDAPObjectsService
from apps.ldapconn.models import LDAPNisNetgroup, LDAPSudoRule
from rest_framework import viewsets

from .models import SudoCommand, SudoCommandRole, SudoHost, SudoHostGroup, SudoRule
from .serializers import (
    SudoCommandRoleCreateSerializer,
    SudoCommandRoleListDetailSerializer,
    SudoCommandRolePutPatchSerializer,
    SudoCommandSerializer,
    SudoHostGroupCreateSerializer,
    SudoHostGroupListDetailSerializer,
    SudoHostGroupPutPatchSerializer,
    SudoHostSerializer,
    SudoRuleCreateSerializer,
    SudoRuleListDetailSerializer,
    SudoRulePutPatchSerializer,
)


class SudoCommandRoleViewSet(viewsets.ModelViewSet):
    queryset = SudoCommandRole.objects.all()

    action_serializer_classes = {
        "list": SudoCommandRoleListDetailSerializer,
        "retrieve": SudoCommandRoleListDetailSerializer,
        "update": SudoCommandRolePutPatchSerializer,
        "partial_update": SudoCommandRolePutPatchSerializer,
        "create": SudoCommandRoleCreateSerializer,
    }

    def get_serializer_context(self):
        return {"request": self.request}

    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.action]
        except (KeyError, AttributeError):
            return super(SudoCommandRoleViewSet, self).get_serializer_class()

    def destroy(self, request, *args, **kwargs):
        sudo_command_role = self.get_object()
        sudo_rules = list(sudo_command_role.sudorule_set.all())
        response = super().destroy(request, *args, **kwargs)
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        sudo_command_role = self.get_object()
        sudo_rules = sudo_command_role.sudorule_set.all()
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        sudo_command_role = self.get_object()
        sudo_rules = sudo_command_role.sudorule_set.all()
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return response


class SudoHostGroupViewSet(viewsets.ModelViewSet):
    queryset = SudoHostGroup.objects.all()
    action_serializer_classes = {
        "list": SudoHostGroupListDetailSerializer,
        "retrieve": SudoHostGroupListDetailSerializer,
        "update": SudoHostGroupPutPatchSerializer,
        "partial_update": SudoHostGroupPutPatchSerializer,
        "create": SudoHostGroupCreateSerializer,
    }

    def get_serializer_context(self):
        return {"request": self.request}

    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.action]
        except (KeyError, AttributeError):
            return super(SudoHostGroupViewSet, self).get_serializer_class()

    def destroy(self, request, *args, **kwargs):
        sudo_host_group = self.get_object()
        sudo_rules = list(sudo_host_group.sudorule_set.all())
        parents = list(sudo_host_group.parents.all())
        ldap_service = LDAPObjectsService(LDAPNisNetgroup)
        ldap_service.destroy_by_instance(sudo_host_group)
        response = super().destroy(request, *args, **kwargs)
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        for parent in parents:
            LDAPNisNetgroup.create_or_update_nis_netgroup(parent)
        return response

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = SudoHostGroup.objects.get(pk=response.data["id"])
        LDAPNisNetgroup.create_or_update_nis_netgroup(instance)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        instance = self.get_object()
        LDAPNisNetgroup.create_or_update_nis_netgroup(instance)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        instance = self.get_object()
        LDAPNisNetgroup.create_or_update_nis_netgroup(instance)
        return response


class SudoHostViewSet(viewsets.ModelViewSet):
    queryset = SudoHost.objects.all()
    serializer_class = SudoHostSerializer

    def destroy(self, request, *args, **kwargs):
        sudo_host = self.get_object()
        sudo_rules = list(sudo_host.sudorule_set.all())
        response = super().destroy(request, *args, **kwargs)
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        sudo_host = self.get_object()
        sudo_rules = sudo_host.sudorule_set.all()
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        sudo_host = self.get_object()
        sudo_rules = sudo_host.sudorule_set.all()
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return response


class SudoCommandViewSet(viewsets.ModelViewSet):
    queryset = SudoCommand.objects.all()
    serializer_class = SudoCommandSerializer

    def destroy(self, request, *args, **kwargs):
        sudo_command = self.get_object()
        sudo_rules = list(sudo_command.sudorule_set.all())
        response = super().destroy(request, *args, **kwargs)
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        sudo_command = self.get_object()
        sudo_rules = sudo_command.sudorule_set.all()
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        sudo_command = self.get_object()
        sudo_rules = sudo_command.sudorule_set.all()
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return response


class SudoRuleViewSet(viewsets.ModelViewSet):
    queryset = SudoRule.objects.all()

    action_serializer_classes = {
        "list": SudoRuleListDetailSerializer,
        "retrieve": SudoRuleListDetailSerializer,
        "update": SudoRulePutPatchSerializer,
        "partial_update": SudoRulePutPatchSerializer,
        "create": SudoRuleCreateSerializer,
    }

    def get_serializer_context(self):
        return {"request": self.request}

    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.action]
        except (KeyError, AttributeError):
            return super(SudoRuleViewSet, self).get_serializer_class()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        ldap_service = LDAPObjectsService(LDAPSudoRule)
        ldap_service.destroy_by_instance(instance)
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = SudoRule.objects.get(pk=response.data["id"])
        LDAPSudoRule.create_or_update_sudo_rule(instance)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        instance = self.get_object()
        LDAPSudoRule.create_or_update_sudo_rule(instance)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        instance = self.get_object()
        LDAPSudoRule.create_or_update_sudo_rule(instance)
        return response
