from rest_framework import viewsets

from .models import LnxShell, LnxGroup
from .serializers import LnxGroupSerializer, LnxShellSerializer


class LnxShellViewSet(viewsets.ModelViewSet):
    queryset = LnxShell.objects.all()
    serializer_class = LnxShellSerializer

class LnxGroupViewSet(viewsets.ModelViewSet):
    queryset = LnxGroup.objects.all()
    serializer_class = LnxGroupSerializer
