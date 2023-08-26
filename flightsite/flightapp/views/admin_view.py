from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..logics.admin import AdminLogic
from ..serializers.admin import AdminSerializer
from ..logics.permission import user_permissions


class AdminsList(generics.GenericAPIView,
                 mixins.CreateModelMixin, 
                 mixins.ListModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = AdminLogic()
    queryset = logic.get_all()
    serializer_class = AdminSerializer
    
    @method_decorator(user_permissions('flightapp.add_administrator'))
    def post(self, request, *args, **kwargs):
        """
        Create a new admin.
        Makes him a superuser
        """
        return self.create(request, *args, **kwargs)
        

    @method_decorator(user_permissions('flightapp.view_administrator'))
    def get(self, request, *args, **kwargs):
        """
        List of all admins.
        """
        return self.list(request, *args, **kwargs)
    


class AdminDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                     
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing an admin id.
    """
    logic = AdminLogic()
    queryset = logic.get_all()
    serializer_class = AdminSerializer

    @method_decorator(user_permissions('flightapp.view_administrator'))
    def get(self, request, *args, **kwargs):
        """
        Get a specific admin.
        """
        return self.retrieve(request, *args, **kwargs)


    @method_decorator(user_permissions('flightapp.change_administrator'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific admin.
        """
        print("request.data",request.data)
        return self.update(request, *args, **kwargs)
    

    @method_decorator(user_permissions('flightapp.delete_administrator'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific admin and associated user.
        """
        
        admin_instance = self.get_object()
        self.logic.delete_admin_with_user(admin_instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    



class GetAdminByUserID(APIView):
    # Im using this view because if i would have used the get user by id mixin view, i would have problem with the permissions
    logic = AdminLogic()

    def get(self, request, *args, **kwargs):
        request_user_id = request.user.id
        return self.logic.get_admin_by_user_id(request_user_id)
