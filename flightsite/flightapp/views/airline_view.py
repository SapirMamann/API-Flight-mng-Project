from rest_framework import mixins, generics
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin

from ..logics.airline import AirlineLogic
from ..serializers.airline import AirlineCompanySerializer

from django.utils.decorators import method_decorator
from ..logics.permission import user_permissions


class AirlinesList(generics.GenericAPIView,
                   PermissionRequiredMixin,
                   mixins.CreateModelMixin, 
                   mixins.ListModelMixin):
    """
    Handles POST and GET requests
    """
    logic = AirlineLogic()
    queryset = logic.get_all()
    serializer_class = AirlineCompanySerializer
    permission_required = 'add_airlinecompany'
    

    def post(self, request, *args, **kwargs):
        """
        havnt tried
        Create a new airline company
        """
        return self.create(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):    
        """
        works
        List of all Airline companies (displays only names)
        """
        return self.list(request, *args, **kwargs)
    


class AirlineDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                     
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing an airline id
    """
    logic = AirlineLogic()
    queryset = logic.get_all()
    serializer_class = AirlineCompanySerializer

    def get(self, request, *args, **kwargs):
        """
        works 24.03 15:35
        Getting a specific airline
        """
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        """
        Updating a specific airline
        """
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        """
        Delete a specific airline
        """
        return self.destroy(request, *args, **kwargs)