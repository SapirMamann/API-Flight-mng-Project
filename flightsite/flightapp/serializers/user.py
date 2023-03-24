from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'     #delete id 
        

    # def validate(self, attrs):
    #     pass
    
    # def validate_useranem():
    #     # ...
    #     pass