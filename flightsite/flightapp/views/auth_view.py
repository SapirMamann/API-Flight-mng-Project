from rest_framework.views  import APIView, Response, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework import generics
from rest_framework.exceptions import APIException
from django.contrib.auth import logout

from ..serializers.auth import RegisterSerializer
from ..serializers.user import UserSerializer
from ..models import User 


from django.utils.decorators import method_decorator
from ..logics.permission import user_permissions

class RegisterView(generics.CreateAPIView):     #why we dont use self here?
    queryset = User.objects.all()
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
            logout(request)
            return Response({'message': 'Successfully logged out.'})