from rest_framework import viewsets, mixins
from .serializers import (LDAPUserSerializer,
    LDAPGroupSerializer, LDAPSudoRuleSerializer)
from .ldap import LDAPObjectsService, create_sudo_rule, modify_user, search_by_sid, search_by_guid
from .models import LDAPUser, LDAPGroup, LDAPSudoRule
from django.http import JsonResponse
from rest_framework.response import Response
from apps.ldapconfig.models import LDAPConfig
from apps.lnxusers.models import LnxUser
from django.db import transaction


def create_sudo_rule_view(request):
    ''' Test code for sudorule creation and user/groups updates
    '''
    create_sudo_rule()
    modify_user()
    search_by_sid()
    search_by_guid()
    return JsonResponse({"hola": "hello world!"})

@transaction.atomic
def get_notused_id(request):
    ''' this method will be used to create users and groups with auto 
        assignment id. Useful for users and groups creation.
    '''

    ldap_conf = LDAPConfig.objects.first()
    min_id, max_id = ldap_conf.get_user_min(), ldap_conf.get_user_max()
    pool = set(range(min_id, max_id + 1)) # large pools not accepted, limit the range <= 1Millon

    used_ids = set(LnxUser.objects.values_list('uid_number', flat=True))

    available_numbers = pool - used_ids  # Subtract used numbers from pool

    return JsonResponse({"free_id": available_numbers.pop()})

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
