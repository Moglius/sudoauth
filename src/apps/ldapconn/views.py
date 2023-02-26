from rest_framework import generics
from .serializers import (LDAPUserSerializer,
    LDAPGroupSerializer)
from .ldap import LDAPObjectsService
from .models import LDAPUser, LDAPGroup


class LDAPUserView(generics.ListAPIView):
    serializer_class = LDAPUserSerializer

    def get_queryset(self):
        ldap_service = LDAPObjectsService(LDAPUser)
        name = self.request.query_params.get('name')
        users = list(ldap_service.get_objects())
        if name:
            return [user for user in users if user.apply_filter(name)]
        return users


class LDAPGroupView(generics.ListAPIView):
    serializer_class = LDAPGroupSerializer

    def get_queryset(self):
        ldap_service = LDAPObjectsService(LDAPGroup)
        name = self.request.query_params.get('name')
        groups = list(ldap_service.get_objects())
        if name:
            return [group for group in groups if group.apply_filter(name)]
        return groups
