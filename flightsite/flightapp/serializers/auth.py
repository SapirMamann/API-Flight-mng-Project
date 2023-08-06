from rest_framework import serializers
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate



class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    # user_role = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    
    def validate_password(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        #Set user's password
        user.set_password(validated_data['password'])
        user.save()
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