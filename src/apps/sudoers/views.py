from rest_framework import viewsets

from .models import SudoRule
from .serializers import SudoRuleSerializer


class SudoRuleViewSet(viewsets.ModelViewSet):
    queryset = SudoRule.objects.all()
    serializer_class = SudoRuleSerializer
