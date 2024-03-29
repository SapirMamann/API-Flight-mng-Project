from rest_framework import mixins, generics
from django.utils.decorators import method_decorator

from ..logics.country import CountryLogic
from ..serializers.country import CountrySerializer
from ..logics.permission import user_permissions


class CountriesList(generics.GenericAPIView, 
                    mixins.ListModelMixin, 
                    mixins.CreateModelMixin):
    """
    Handles POST and GET requests
    """
    logic = CountryLogic()
    queryset = logic.get_all()
    serializer_class = CountrySerializer

    @method_decorator(user_permissions('flightapp.add_country'))
    def post(self, request, *args, **kwargs):
        """
        Add country. 
        """
        return self.create(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        """
        This method has no permission decorator because anonymous users can view countries too.
        List of all countries.
        """
        return self.list(request, *args, **kwargs)
    


class CountryDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                     
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing a country id.
    """
    logic = CountryLogic()
    queryset = logic.get_all()
    serializer_class = CountrySerializer

    @method_decorator(user_permissions('flightapp.view_country'))
    def get(self, request, *args, **kwargs):
        """
        Getting a specific country.
        """
        return self.retrieve(request, *args, **kwargs)


    @method_decorator(user_permissions('flightapp.change_country'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific country.
        """
        return self.update(request, *args, **kwargs)
    

    @method_decorator(user_permissions('flightapp.delete_country'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific country.
        """
        return self.destroy(request, *args, **kwargs)