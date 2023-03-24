from rest_framework.views  import APIView, Response, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework import generics
from django.contrib.auth import logout

from ..serializers.auth import RegisterSerializer
from ..models import User 


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class RefreshTokenView():
    pass    


class LoginView(generics.CreateAPIView):
    pass


class LogoutView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
            logout(request)
            return Response({'message': 'Successfully logged out.'})