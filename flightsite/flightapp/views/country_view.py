from rest_framework import mixins, generics

from ..logics.country import CountryLogic
from ..serializers.country import CountrySerializer


class CountriesList(generics.GenericAPIView, 
                    mixins.ListModelMixin, 
                    mixins.CreateModelMixin):
    """
    Handles POST and GET requests
    """
    logic = CountryLogic()
    queryset = logic.get_all()
    serializer_class = CountrySerializer

    def post(self, request, *args, **kwargs):
        """
        works 24.03 15:50
        Add country. 
        """
        return self.create(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        """
        works 24.03 15:45
        List of all countries.
        """
        return self.list(request, *args, **kwargs)
    


class CountryDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                     
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing an country id.
    """
    logic = CountryLogic()
    queryset = logic.get_all()
    serializer_class = CountrySerializer

    def get(self, request, *args, **kwargs):
        """
        works 24.03 15:45
        Getting a specific country.
        """
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        """
        works 24.03 15:50
        Updating a specific country.
        """
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        """
        works 24.03 16:00
        Delete a specific country.
        """
        return self.destroy(request, *args, **kwargs)