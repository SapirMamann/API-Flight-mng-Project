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
    groups = serializers.CharField(required=True)


    class Meta:
        model = User
        fields = ('id','username', 'password', 'password2', 'email', 'groups')


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        print(attrs)
        return attrs
    
    
    def create(self, validated_data):
        # Extract the groups from validated_data. If the key 'groups' is present, the value will be removed from the dictionary and assigned to the variable group_names. If the key is not present, it will default to an empty list [].
        print(validated_data)
        group_name = validated_data['groups']
        print(group_name)

        try:
            # Create the user
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
            )
        except Exception as e:
            error_message = f"An error occurred when creating user: {e}"
            # logging.error(error_message)
            raise serializers.ValidationError(error_message)

        # Set user's password
        user.set_password(validated_data['password'])
        user.save()

        # Assign the user to the group
        try:
            group = Group.objects.get(name=group_name)
            group.user_set.add(user)
            if group_name == 'Administrator':
                user.is_staff = True
                user.is_superuser = True
                user.save()
                
            print(user)
            print(user.get_all_permissions())
            return user    
        except Group.DoesNotExist:
            print("Group does not exist")
            return Response({"error": "Group does not exist"}, status=400)
        except Exception as e:
            error_message = f"An error occurred: {e}"
            # logging.error(error_message)
            raise serializers.ValidationError(error_message)


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