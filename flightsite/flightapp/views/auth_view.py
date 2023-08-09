from rest_framework.views  import APIView, Response
from rest_framework import generics, status, permissions
from django.contrib.auth import logout
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from ..serializers.auth import RegisterSerializer, CustomTokenObtainPairSerializer
from ..serializers.user import UserSerializer
from ..logics.permission import user_permissions
from ..logics.user import UserLogic
from django.contrib.auth.models import User, Group


class RegisterView(generics.CreateAPIView):
    """
    Creating a new user, has a built-in hashed password
    """
    permission_classes = [permissions.AllowAny]
    logic = UserLogic()
    queryset = logic.get_all()
    serializer_class = RegisterSerializer
    
    # def perform_create(self, serializer):
    #     # user = serializer.save()
    #     print(serializer)

    #     # group_names = serializer.validated_data.get('groups', [])  # Get the group names from the serializer data

    #     # # Assign a group to the user here
    #     # groups = [Group.objects.get_or_create(name=group_name)[0] for group_name in group_names]
    #     # user.groups.set(groups)

    #     # Return the user data with a success message
    #     data = serializer.data
    #     data['message'] = 'User registered successfully.'
    #     return Response(data, status=status.HTTP_201_CREATED)



class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Login.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomTokenObtainPairSerializer

    # def post(self, request, *args, **kwargs):
    #     print(f"Received POST request with data: {request.data}")
    #     response = super().post(request, *args, **kwargs)
    #     print(f"Response data: {response.data}")
    #     return response



class LogoutView(APIView):
    """
    Logout. 
    """
    # permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)