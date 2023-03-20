from rest_framework import viewsets

from apps.ldapconn.ldap import LDAPObjectsService
from apps.ldapconn.models import LDAPUser, LDAPGroup
from apps.sudoers.models import SudoUser
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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        SudoUser.objects.get(pk=instance.related_group.pk).delete()
        ldap_service = LDAPObjectsService(LDAPGroup)
        ldap_service.clear_by_instance(instance)
        return super().destroy(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        # TODO: modify fields on LDAP entry
        return super().partial_update(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        # TODO: Modify fields on LDAP entry
        return super().update(request, *args, **kwargs)


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
        SudoUser.objects.get(pk=instance.related_user.pk).delete()
        ldap_service = LDAPObjectsService(LDAPUser)
        ldap_service.clear_by_instance(instance)
        return super().destroy(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        # TODO: modify fields on LDAP entry
        return super().partial_update(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        # TODO: Modify fields on LDAP entry
        return super().update(request, *args, **kwargs)
