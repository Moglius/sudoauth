from rest_framework import viewsets

from apps.ldapconn.models import LDAPSudoRule
from apps.ldapconn.ldap import LDAPObjectsService
from .models import SudoRule
from .serializers import (SudoRuleListDetailSerializer,
    SudoRulePutPatchSerializer, SudoRuleCreateSerializer)


class SudoRuleViewSet(viewsets.ModelViewSet):
    queryset = SudoRule.objects.all()

    action_serializer_classes = {
        'list': SudoRuleListDetailSerializer, 
        'retrieve': SudoRuleListDetailSerializer,
        'update': SudoRulePutPatchSerializer,
        'partial_update': SudoRulePutPatchSerializer,
        'create': SudoRuleCreateSerializer
    }

    def get_serializer_context(self):
        return {'request': self.request}

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
        instance = SudoRule.objects.get(pk=response.data['pk'])
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
