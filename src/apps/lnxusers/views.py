from rest_framework import viewsets

from .models import LnxShell, LnxGroup, LnxUser
from .serializers import (
    LnxGroupSerializer, LnxShellSerializer,
    LnxUserSerializer
)


class LnxShellViewSet(viewsets.ModelViewSet):
    queryset = LnxShell.objects.all()
    serializer_class = LnxShellSerializer


class LnxGroupViewSet(viewsets.ModelViewSet):
    queryset = LnxGroup.objects.all()
    serializer_class = LnxGroupSerializer


class LnxUserViewSet(viewsets.ModelViewSet):
    queryset = LnxUser.objects.all()
    serializer_class = LnxUserSerializer
