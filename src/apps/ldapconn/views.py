from rest_framework import generics, viewsets, mixins
from .serializers import (LDAPUserSerializer,
    LDAPGroupSerializer, LDAPSudoRuleSerializer)
from .ldap import LDAPObjectsService, create_sudo_rule, modify_user, search_by_sid, search_by_guid
from .models import LDAPUser, LDAPGroup, LDAPSudoRule
from django.http import JsonResponse
from rest_framework.response import Response


def create_sudo_rule_view(request):
    create_sudo_rule()
    #modify_user()
    search_by_sid()
    search_by_guid()
    return JsonResponse({"hola": "hello world!"})


class ListRetrieveViewSet(mixins.ListModelMixin,
    mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass


class LDAPUserViewSet(ListRetrieveViewSet):

    serializer_class = LDAPUserSerializer

    def get_queryset(self):
        ldap_service = LDAPObjectsService(LDAPUser)
        name = self.request.query_params.get('name')
        users = list(ldap_service.get_objects())
        if name:
            return [user for user in users if user.apply_filter(name)]
        return users

    def retrieve(self, request, *args, pk=None, **kwargs):
        ldap_service = LDAPObjectsService(LDAPUser)
        user = ldap_service.get_object(pk)
        serializer = LDAPUserSerializer(user)
        return Response(serializer.data)


class LDAPGroupViewSet(ListRetrieveViewSet):

    serializer_class = LDAPGroupSerializer

    def get_queryset(self):
        ldap_service = LDAPObjectsService(LDAPGroup)
        name = self.request.query_params.get('name')
        groups = list(ldap_service.get_objects())
        if name:
            return [group for group in groups if group.apply_filter(name)]
        return groups

    def retrieve(self, request, *args, pk=None, **kwargs):
        ldap_service = LDAPObjectsService(LDAPGroup)
        user = ldap_service.get_object(pk)
        serializer = LDAPGroupSerializer(user)
        return Response(serializer.data)


class LDAPSudoRuleViewSet(ListRetrieveViewSet):

    serializer_class = LDAPSudoRuleSerializer

    def get_queryset(self):
        ldap_service = LDAPObjectsService(LDAPSudoRule)
        name = self.request.query_params.get('name')
        rules = list(ldap_service.get_objects())
        if name:
            return [rule for rule in rules if rule.apply_filter(name)]
        return rules

    def retrieve(self, request, *args, pk=None, **kwargs):
        ldap_service = LDAPObjectsService(LDAPSudoRule)
        user = ldap_service.get_object(pk)
        serializer = LDAPSudoRuleSerializer(user)
        return Response(serializer.data)
