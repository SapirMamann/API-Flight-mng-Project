from rest_framework import mixins, generics
from django.contrib.auth.mixins import PermissionRequiredMixin  #inherit for class 
from django.contrib.auth.decorators import permission_required  #decorator for function

from ..logics.admin import AdminLogic
from ..serializers.admin import AdminSerializer


from django.utils.decorators import method_decorator
from ..logics.permission import user_permissions

class AdminsList(generics.GenericAPIView,
                 PermissionRequiredMixin,
                 mixins.CreateModelMixin, 
                 mixins.ListModelMixin):
    """
    Handles POST and GET requests
    """
    # permission_required = ()
    logic = AdminLogic()
    queryset = logic.get_all()
    serializer_class = AdminSerializer
    
    def post(self, request, *args, **kwargs):
        """
        works 24.03 13:14
        Create a new admin
        """
        return self.create(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        """
        works 24.03 13:14
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

    def get(self, request, *args, **kwargs):
        """
        works 24.03 13:20
        Get a specific admin
        """
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        """
        works 24.03 13:24
        Updating a specific admin
        """
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        """
        **********havnt been tested****************
        Delete a specific admin
        """
        return self.destroy(request, *args, **kwargs)