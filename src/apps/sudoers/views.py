from rest_framework import viewsets

from apps.ldapconn.models import LDAPSudoRule
from apps.ldapconn.ldap import LDAPObjectsService
from .models import SudoRule
from .serializers import SudoRuleSerializer


class SudoRuleViewSet(viewsets.ModelViewSet):
    queryset = SudoRule.objects.all()
    serializer_class = SudoRuleSerializer

    def destroy(self, request, *args, pk=None, **kwargs):
        ldap_service = LDAPObjectsService(LDAPSudoRule)
        ldap_service.destroy_by_instance(SudoRule.objects.get(pk=pk))
        return super().destroy(request, *args, **kwargs)
