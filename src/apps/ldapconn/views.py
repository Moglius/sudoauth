from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from .serializers import (LDAPUserSerializer, LDAPGroupSerializer,
    LDAPUserGroupCreationSerializer, LDAPSudoRuleSerializer)
from .models import LDAPUser, LDAPGroup, LDAPSudoRule


class LDAPViewSet(mixins.ListModelMixin,
    mixins.RetrieveModelMixin, mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    pass


class LDAPUserViewSet(LDAPViewSet):

    serializer_class = LDAPUserSerializer

    def get_queryset(self):
        users = LDAPUser.get_objects_list()
        name = self.request.query_params.get('name')
        if name:
            return [user for user in users if user.apply_filter(name)]
        return users

    action_serializer_classes = {
        'list': LDAPUserSerializer, 
        'retrieve': LDAPUserSerializer,
        'create': LDAPUserGroupCreationSerializer
    }

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.action]
        except (KeyError, AttributeError):
            return super(LDAPUserViewSet, self).get_serializer_class()

    def retrieve(self, request, *args, pk=None, **kwargs):
        user = LDAPUser.get_object_by_guid(pk)
        serializer = LDAPUserSerializer(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = LDAPUserGroupCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = LDAPUser.create_object_by_guid(serializer.get_guid())
            serializer = LDAPUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LDAPGroupViewSet(LDAPViewSet):

    serializer_class = LDAPGroupSerializer

    def get_queryset(self):
        groups = LDAPGroup.get_objects_list()
        name = self.request.query_params.get('name')
        if name:
            return [group for group in groups if group.apply_filter(name)]
        return groups

    action_serializer_classes = {
        'list': LDAPGroupSerializer, 
        'retrieve': LDAPGroupSerializer,
        'create': LDAPUserGroupCreationSerializer
    }

    def get_serializer_context(self):
        return {'request': self.request}

    def get_serializer_class(self):
        try:
            return self.action_serializer_classes[self.action]
        except (KeyError, AttributeError):
            return super(LDAPGroupViewSet, self).get_serializer_class()

    def retrieve(self, request, *args, pk=None, **kwargs):
        group = LDAPGroup.get_object_by_guid(pk)
        serializer = LDAPGroupSerializer(group)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = LDAPUserGroupCreationSerializer(data=request.data)
        if serializer.is_valid():
            group = LDAPGroup.create_object_by_guid(serializer.get_guid())
            serializer = LDAPGroupSerializer(group)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LDAPSudoRuleViewSet(LDAPViewSet):

    serializer_class = LDAPSudoRuleSerializer
    http_method_names = ['get', 'head']

    def get_queryset(self):
        rules = LDAPSudoRule.get_objects_list()
        name = self.request.query_params.get('name')
        if name:
            return [rule for rule in rules if rule.apply_filter(name)]
        return rules

    def retrieve(self, request, *args, pk=None, **kwargs):
        sudorule = LDAPSudoRule.get_object_by_guid(pk)
        serializer = LDAPSudoRuleSerializer(sudorule)
        return Response(serializer.data)
