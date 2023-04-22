from rest_framework import viewsets
from rest_framework.serializers import ValidationError

from apps.ldapconn.models import (LDAPUser, LDAPGroup,
    LDAPSudoRule)
from apps.ldapconfig.models import LDAPConfig
from .models import LnxShell, LnxGroup, LnxUser
from .serializers import (LnxGroupSerializer, LnxShellSerializer,
    LnxUserPutPatchSerializer, LnxUserListDetailSerializer)


class LnxShellViewSet(viewsets.ModelViewSet):
    queryset = LnxShell.objects.all()
    serializer_class = LnxShellSerializer

    def _set_lnxuser_default_shell(self, shell: LnxShell):
        default_shell = LDAPConfig.get_default_shell()
        for lnxuser in shell.get_attached_lnxusers():
            lnxuser.set_shell(default_shell)
            LDAPUser.update_lnxuser(lnxuser)
        return default_shell

    def _update_shell_ldap_entries(self, shell: LnxShell):
        for lnxuser in shell.get_attached_lnxusers():
            LDAPUser.update_lnxuser(lnxuser)
        return shell

    def destroy(self, request, *args, **kwargs):
        shell = self.get_object()
        if shell.is_built_in() or shell.is_default_shell():
            raise ValidationError('This shell is either seleted as default in your config '\
                                  'or it is an app built-in shell, Can not be deleted.')
        self._set_lnxuser_default_shell(shell)
        return super().destroy(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        shell = self.get_object()
        self._update_shell_ldap_entries(shell)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        shell = self.get_object()
        self._update_shell_ldap_entries(shell)
        return response


class LnxGroupViewSet(viewsets.ModelViewSet):
    queryset = LnxGroup.objects.all()
    serializer_class = LnxGroupSerializer
    http_method_names = ['get', 'delete', 'head', 'put', 'patch']

    def _set_lnxuser_default_group(self, instance: LnxGroup):
        default_group = LDAPConfig.get_default_group()
        for lnxuser in instance.get_attached_lnxusers():
            lnxuser.set_group(default_group)
            LDAPUser.update_lnxuser(lnxuser)
        return default_group

    def _remove_lnxgroup_from_sudorules(self, sudorules):
        for sudo_rule in sudorules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return sudorules

    def _set_sudorule_default_runas(self, sudorules, lnxgroup):
        default_group = LnxGroup.objects.filter(groupname='root').first()
        for sudo_rule in sudorules:
            sudo_rule.set_default_runas_group(lnxgroup, default_group)
        return sudorules

    def destroy(self, request, *args, **kwargs):
        lnxgroup = self.get_object()
        if lnxgroup.is_default_group():
            raise ValidationError('This group is seleted as default in your config.'\
                                  'Can not be deleted.')
        sudorules = lnxgroup.get_attached_sudorules()
        self._set_lnxuser_default_group(lnxgroup)
        self._set_sudorule_default_runas(sudorules, lnxgroup)
        LDAPGroup.clear_lnxgroup(lnxgroup)
        response = super().destroy(request, *args, **kwargs)
        self._remove_lnxgroup_from_sudorules(sudorules)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        lnxgroup = self.get_object()
        LDAPGroup.update_lnxgroup(lnxgroup)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        lnxgroup = self.get_object()
        LDAPGroup.update_lnxgroup(lnxgroup)
        return response


class LnxUserViewSet(viewsets.ModelViewSet):
    queryset = LnxUser.objects.all()
    http_method_names = ['get', 'delete', 'head', 'put', 'patch']

    action_serializer_classes = {
        'list': LnxUserListDetailSerializer, 
        'retrieve': LnxUserListDetailSerializer,
        'update': LnxUserPutPatchSerializer,
        'partial_update': LnxUserPutPatchSerializer
    }

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.action]
        except (KeyError, AttributeError):
            return super(LnxUserViewSet, self).get_serializer_class()

    def _remove_lnxuser_from_sudorules(self, sudo_rules):
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return sudo_rules

    def _set_sudorule_default_runas(self, sudorules, lnxuser):
        default_user = LnxUser.objects.filter(username='root').first()
        for sudo_rule in sudorules:
            sudo_rule.set_default_runas_user(lnxuser, default_user)
        return sudorules

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        sudo_rules = instance.get_attached_sudorules()
        self._set_sudorule_default_runas(sudo_rules, instance)
        LDAPUser.clear_lnxuser(instance)
        response = super().destroy(request, *args, **kwargs)
        self._remove_lnxuser_from_sudorules(sudo_rules)
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        lnxuser = self.get_object()
        LDAPUser.update_lnxuser(lnxuser)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        lnxuser = self.get_object()
        LDAPUser.update_lnxuser(lnxuser)
        return response
