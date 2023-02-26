from rest_framework import generics
from .serializers import LDAPUserSerializer
from .ldap import LDAPObjectsService


class LDAPUserView(generics.ListAPIView):
    serializer_class = LDAPUserSerializer

    def get_queryset(self):
        ldap_service = LDAPObjectsService()
        return list(ldap_service.get_objects())
