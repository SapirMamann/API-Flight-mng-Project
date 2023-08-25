from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'     #delete id 
        

    def validate_username(self, username):
        if len(username) < 2 or len(username) > 100:
            raise serializers.ValidationError("Username length must be between 3 to 99.")        #i can raise a better error message
        # elif username contains bad words
        existing_user = User.objects.filter(username=username).exclude(pk=self.instance.pk)
        if existing_user.exists():
            raise serializers.ValidationError("This username is already in use.")
        
        return username
    

