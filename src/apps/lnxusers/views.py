from rest_framework import viewsets
from rest_framework.serializers import ValidationError

from apps.ldapconn.models import LDAPUser, LDAPGroup, LDAPSudoRule
from apps.sudoers.models import SudoUser
from apps.ldapconfig.models import LDAPConfig
from .models import LnxShell, LnxGroup, LnxUser
from .serializers import (
    LnxGroupSerializer, LnxShellSerializer,
    LnxUserPutPatchSerializer, LnxUserListDetailSerializer
)


class LnxShellViewSet(viewsets.ModelViewSet):
    queryset = LnxShell.objects.all()
    serializer_class = LnxShellSerializer


class LnxGroupViewSet(viewsets.ModelViewSet):
    queryset = LnxGroup.objects.all()
    serializer_class = LnxGroupSerializer
    http_method_names = ['get', 'delete', 'head', 'put', 'patch']

    def _set_lnxuser_default_group(self, instance):
        default_group = LDAPConfig.get_default_group()
        for lnxuser in instance.lnxuser_set.all():
            lnxuser.primary_group = default_group
            lnxuser.save()
            LDAPUser.update_lnxuser(lnxuser)
        return default_group

    def _remove_sudouser_from_sudorules(self, instance):
        sudo_user = SudoUser.objects.get(pk=instance.related_group.pk)
        sudo_rules = list(sudo_user.sudorule_set.all())
        sudo_user.delete()
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        return sudo_rules

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.default_group_set.all():
            raise ValidationError('This group is seleted as default in your config.'\
                                  'Can not be deleted.')
        self._set_lnxuser_default_group(instance)
        self._remove_sudouser_from_sudorules(instance)
        LDAPGroup.clear_lnxgroup(instance)
        return super().destroy(request, *args, **kwargs)

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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        sudo_user = SudoUser.objects.get(pk=instance.related_user.pk)
        sudo_rules = list(sudo_user.sudorule_set.all())
        sudo_user.delete()
        for sudo_rule in sudo_rules:
            LDAPSudoRule.create_or_update_sudo_rule(sudo_rule)
        LDAPUser.clear_lnxuser(instance)
        return super().destroy(request, *args, **kwargs)

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
