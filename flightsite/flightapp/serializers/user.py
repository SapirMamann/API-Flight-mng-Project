from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'     #delete id 
        

    def validate_username(self, username):
        if len(username) < 2 or len(username) > 100:
            raise serializers.ValidationError("Username length must be between 3 to 99.")        #i can raise a better error message
        # elif username contains bad words
        return username
    
    