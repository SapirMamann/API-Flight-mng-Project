from django.contrib.auth import logout
from django.contrib.auth.views import PasswordChangeView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User, Group
from rest_framework.views  import APIView, Response
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated   

from ..serializers.auth import RegisterSerializer, CustomTokenObtainPairSerializer, ChangePasswordSerializer
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
    


class UpdatePassword(APIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]}, 
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)