from rest_framework import mixins, generics
from django.utils.decorators import method_decorator

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
    
    @method_decorator(user_permissions('add_administrator'))
    def post(self, request, *args, **kwargs):
        """
        Create a new admin.
        """
        return self.create(request, *args, **kwargs)


    @method_decorator(user_permissions('view_administrator'))
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

    @method_decorator(user_permissions('view_administrator'))
    def get(self, request, *args, **kwargs):
        """
        Get a specific admin.
        """
        return self.retrieve(request, *args, **kwargs)


    @method_decorator(user_permissions('change_administrator'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific admin.
        """
        return self.update(request, *args, **kwargs)
    

    @method_decorator(user_permissions('delete_administrator'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific admin.
        """
        return self.destroy(request, *args, **kwargs)