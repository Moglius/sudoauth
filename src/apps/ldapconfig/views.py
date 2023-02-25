from rest_framework import viewsets

from .models import (DNSHost, LDAPDn,
    LDAPConfig)
from .serializers import (DNSHostSerializer,
    LDAPDnSerializer, LDAPConfigSerializer)


class DNSHostViewSet(viewsets.ModelViewSet):
    queryset = DNSHost.objects.all()
    serializer_class = DNSHostSerializer


class LDAPDnViewSet(viewsets.ModelViewSet):
    queryset = LDAPDn.objects.all()
    serializer_class = LDAPDnSerializer


class LDAPConfigViewSet(viewsets.ModelViewSet):
    queryset = LDAPConfig.objects.all()
    serializer_class = LDAPConfigSerializer
