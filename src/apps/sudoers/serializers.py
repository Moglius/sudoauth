
from rest_framework import serializers

from .models import (
    SudoRule,
    SudoUser,
    SudoHost,
)


class SudoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoUser
        fields = ['username']


class SudoHostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SudoHost
        fields = ['hostname']


class SudoRuleSerializer(serializers.ModelSerializer):
    sudo_user = SudoUserSerializer(many=True)
    sudo_host = SudoHostSerializer(many=True)

    class Meta:
        model = SudoRule
        fields = ['name', 'sudo_user', 'sudo_host']

    def create(self, validated_data): # POST
        sudo_users = validated_data.pop('sudo_user')
        print(sudo_users) 
        return
    
    def update(self, instance, validated_data): # PATCH, PUT
        print(validated_data)
        print(instance) 
        return