from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from apps.ldapconn.models import LDAPSudoRule
from apps.ldapconn.ldap import LDAPObjectsService
from .models import SudoRule
from .serializers import SudoRuleSerializer


class SudoRuleViewSet(viewsets.ModelViewSet):
    queryset = SudoRule.objects.all()
    serializer_class = SudoRuleSerializer

    def destroy(self, request, *args, pk=None, **kwargs):
        sudo_rule = get_object_or_404(SudoRule, pk=pk)
        ldap_service = LDAPObjectsService(LDAPSudoRule)
        ldap_service.destroy_by_instance(sudo_rule)
        return super().destroy(request, *args, **kwargs)
