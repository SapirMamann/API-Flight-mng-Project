from rest_framework import mixins, generics

from ..logics.user import UserLogic
from ..models import User
from ..serializers.user import UserSerializer


class UsersList(generics.GenericAPIView,
                   mixins.CreateModelMixin, 
                   mixins.ListModelMixin):
    """
    Handles POST and GET requests
    """
    logic = UserLogic()
    queryset = logic.get_all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        works 24.03 17:24
        Create a new user. 
        """
        return self.create(request, *args, **kwargs)
    

    def get(self, request, *args, **kwargs):
        """
        works 24.03 17:17
        List of all users.
        """
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