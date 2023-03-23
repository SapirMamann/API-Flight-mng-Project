from rest_framework import serializers

from ..models import Customer, User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 
    def validate(self, attrs):
        pass
    def validate_useranem():
        # ...
        pass