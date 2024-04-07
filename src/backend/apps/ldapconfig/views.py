from rest_framework import viewsets

from .models import DNSHost, LDAPConfig, LDAPDn
from .serializers import DNSHostSerializer, LDAPConfigSerializer, LDAPDnSerializer


class DNSHostViewSet(viewsets.ModelViewSet):
    queryset = DNSHost.objects.all()
    serializer_class = DNSHostSerializer


class LDAPDnViewSet(viewsets.ModelViewSet):
    queryset = LDAPDn.objects.all()
    serializer_class = LDAPDnSerializer


class LDAPConfigViewSet(viewsets.ModelViewSet):
    queryset = LDAPConfig.objects.all()
    serializer_class = LDAPConfigSerializer
