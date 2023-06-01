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

class RegisterView(generics.CreateAPIView):
    """
    Creating a new user, has a built-in hashed password
    """
    permission_classes = [permissions.AllowAny]
    logic = UserLogic()
    queryset = logic.get_all()
    serializer_class = RegisterSerializer



class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Login.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomTokenObtainPairSerializer



class LogoutView(APIView):
    """
    Logout. 
    """
    # permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)