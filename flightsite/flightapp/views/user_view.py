from rest_framework import mixins, generics, permissions
from rest_framework.response import Response

from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from rest_framework.permissions import IsAdminUser

from ..logics.user import UserLogic
from ..models import User
from ..serializers.user import UserSerializer


class UsersList(generics.GenericAPIView,
                PermissionRequiredMixin,
                mixins.CreateModelMixin, 
                mixins.ListModelMixin):
    """
    Handles POST and GET requests
    """
    permission_classes = [permissions.DjangoModelPermissions]
    permission_required = 'flightapp.view_user'

    logic = UserLogic()
    queryset = logic.get_all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        maybe i dont need this because im using auth register
        for admin use
        works 24.03 17:24
        Create a new user.
        """
        return self.create(request, *args, **kwargs)
    

    def get(self, request, *args, **kwargs):
        """
        works 24.03 17:17
        List of all users.
        """
        print(f"User permissions: {request.user.get_all_permissions()}")
        print(f"User permissions: {request.user.has_perm('flightapp.view_user')}")
        # if request.user.has_perm('flightapp.view_user') is False:
        #     return Response('okkkkkk', status=403)

        return self.list(request, *args, **kwargs)



class UserDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                     
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing an user id.
    """    
    logic = UserLogic()
    queryset = logic.get_all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        """
        works 24.03 17:19
        Getting a specific user.
        """
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        """
        works 24.03 17:22
        Updating a specific user.
        """
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        """
        works 24.03 17:26
        Delete a specific user.
        """
        return self.destroy(request, *args, **kwargs)