from rest_framework import mixins, generics

from ..logics.user_role import UserRoleLogic
from ..serializers.user_role import UserRoleSerializer


class UserRolesList(generics.GenericAPIView,
                   mixins.CreateModelMixin, 
                   mixins.ListModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = UserRoleLogic()
    queryset = logic.get_all()
    serializer_class = UserRoleSerializer

    def post(self, request, *args, **kwargs):
        """
        works 24.03 13:00
        Create a new user role.
        """
        return self.create(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):    
        """
        works 24.03 13:00
        List of all user roles.
        """
        return self.list(request, *args, **kwargs)
    


class UserRoleDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                     
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing an user id
    """
    logic = UserRoleLogic()
    queryset = logic.get_all()
    serializer_class = UserRoleSerializer

    def get(self, request, *args, **kwargs):
        """
        works 24.03 16:44
        Getting a specific user role
        """
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        """
        works 24.03 16:49
        Updating a specific user role
        """
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        """
        works 24.03 16:49
        Delete a specific user role
        """
        return self.destroy(request, *args, **kwargs)