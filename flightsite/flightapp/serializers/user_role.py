from rest_framework import serializers

from ..models import UserRoles


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = '__all__'
        
