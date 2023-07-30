from rest_framework import serializers
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate

from ..models import User, UserGroup


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    user_role = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'user_role')

    def validate_password(self, value):
        password2 = self.initial_data.get('password2')
        #need to debugggggggggggggggggg
        #i get the wrong group everytime. 
        #and i tried to change this so it will have its own password validation function but now it has a problem beacuse it gives me array i think
        if value['password'] != value['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        print(value)
        return value
    
    def validate_user_role(self, value):
        # user_role_instance = UserGroup.objects.filter(id=value['user_role']).first()

        # if not user_role_instance:
        #     raise serializers.ValidationError({"user_role": "User Group is bad"})
        # return value
        print(value)

    def create(self, validated_data):
        user_role_instance = UserGroup.objects.filter(id=validated_data['user_role']).first()

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            user_role=user_role_instance,
        )

        #Set user's password
        user.set_password(validated_data['password'])
        user.save()

        #Assign group by name
        choosen_group = Group.objects.get(name=user_role_instance.name) 
        choosen_group.user_set.add(user)

        return user            



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': ('email or password are incorrect!')
    }

    # def validate(self, attrs):
    #     email = attrs.get('email')
    #     password = attrs.get('password')

    #     user = authenticate(email=email, password=password)

    #     if user:
    #         if not user.is_active:
    #             raise AuthenticationFailed(
    #                 self.error_messages['no_active_account'],
    #                 code='no_active_account',
    #             )
    #     else:
    #         raise AuthenticationFailed(
    #             self.error_messages['no_active_account'],
    #             code='no_active_account',
    #         )

    #     data = super().validate(attrs)
    #     return data