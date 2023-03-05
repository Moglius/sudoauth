from rest_framework import generics, viewsets, mixins
from .serializers import (LDAPUserSerializer,
    LDAPGroupSerializer)
from .ldap import LDAPObjectsService, create_sudo_rule, modify_user, search_by_sid, search_by_guid
from .models import LDAPUser, LDAPGroup
from django.http import JsonResponse
from rest_framework.response import Response


def create_sudo_rule_view(request):
    #create_sudo_rule()
    #modify_user()
    search_by_sid()
    search_by_guid()
    return JsonResponse({"hola": "hello world!"})


class ListRetrieveViewSet(mixins.ListModelMixin,
    mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass


class LDAPUserViewSet(ListRetrieveViewSet):

    serializer_class = LDAPUserSerializer
    ldap_service = LDAPObjectsService(LDAPUser)

    def get_queryset(self): 
        name = self.request.query_params.get('name')
        users = list(self.ldap_service.get_objects())
        if name:
            return [user for user in users if user.apply_filter(name)]
        return users

    def retrieve(self, request, *args, pk=None, **kwargs):
        user = self.ldap_service.get_object(pk)
        serializer = LDAPUserSerializer(user)
        return Response(serializer.data)


class LDAPGroupViewSet(ListRetrieveViewSet):

    serializer_class = LDAPGroupSerializer
    ldap_service = LDAPObjectsService(LDAPGroup)

    def get_queryset(self):
        name = self.request.query_params.get('name')
        groups = list(self.ldap_service.get_objects())
        if name:
            return [group for group in groups if group.apply_filter(name)]
        return groups

    def retrieve(self, request, *args, pk=None, **kwargs):
        user = self.ldap_service.get_object(pk)
        serializer = LDAPGroupSerializer(user)
        return Response(serializer.data)
