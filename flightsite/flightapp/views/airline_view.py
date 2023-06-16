from rest_framework import mixins, generics
from django.utils.decorators import method_decorator

from ..logics.airline import AirlineLogic
from ..serializers.airline import AirlineCompanySerializer
from ..logics.permission import user_permissions


class AirlinesList(generics.GenericAPIView,
                   mixins.CreateModelMixin, 
                   mixins.ListModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = AirlineLogic()
    queryset = logic.get_all()
    serializer_class = AirlineCompanySerializer    

    @method_decorator(user_permissions('add_airlinecompany'))
    def post(self, request, *args, **kwargs):
        """
        Create a new airline company.
        """
        return self.create(request, *args, **kwargs)


    @method_decorator(user_permissions('view_airlinecompany'))
    def get(self, request, *args, **kwargs):    
        """
        List of all Airline companies (displays only names).
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

    @method_decorator(user_permissions('view_airlinecompany'))
    def get(self, request, *args, **kwargs):
        """
        Getting a specific airline
        """
        return self.retrieve(request, *args, **kwargs)


    @method_decorator(user_permissions('change_airlinecompany'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific airline
        """
        return self.partial_update(request, *args, **kwargs)


    @method_decorator(user_permissions('delete_airlinecompany'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific airline
        """
        return self.destroy(request, *args, **kwargs)