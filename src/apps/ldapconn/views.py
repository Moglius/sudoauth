from rest_framework import viewsets, mixins
from .serializers import (LDAPUserSerializer, LDAPUserGroupCreationSerializer,
    LDAPGroupSerializer, LDAPSudoRuleSerializer)
from .ldap import LDAPObjectsService, create_sudo_rule, modify_user, search_by_sid, search_by_guid
from .models import LDAPUser, LDAPGroup, LDAPSudoRule
from django.http import JsonResponse
from rest_framework.response import Response
from apps.ldapconfig.models import LDAPConfig
from apps.lnxusers.models import LnxUser
from django.db import transaction
from rest_framework import status


def create_sudo_rule_view(request):
    ''' Test code for sudorule creation and user/groups updates
    '''
    create_sudo_rule()
    modify_user()
    search_by_sid()
    search_by_guid()
    return JsonResponse({"hola": "hello world!"})


class LDAPViewSet(mixins.ListModelMixin,
    mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    pass


class LDAPUserViewSet(LDAPViewSet):

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

    def create(self, request, *args, **kwargs):
        ldap_service = LDAPObjectsService(LDAPUser)
        serializer = LDAPUserGroupCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = ldap_service.create_object_by_guid(serializer.data['objectGUIDHex'])
            serializer = LDAPUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LDAPGroupViewSet(LDAPViewSet):

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

    def create(self, request, *args, **kwargs):
        ldap_service = LDAPObjectsService(LDAPGroup)
        serializer = LDAPUserGroupCreationSerializer(data=request.data)
        if serializer.is_valid():
            group = ldap_service.create_object_by_guid(serializer.data['objectGUIDHex'])
            serializer = LDAPGroupSerializer(group)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LDAPSudoRuleViewSet(LDAPViewSet):

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
