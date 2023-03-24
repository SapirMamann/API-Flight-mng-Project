from rest_framework import mixins, generics

from ..serializers.flight import FlightSerializer 
from ..logics.flight import FlightLogic


class FlightsList(generics.GenericAPIView, 
                 mixins.ListModelMixin, 
                 mixins.CreateModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = FlightLogic()
    queryset = logic.get_all()
    serializer_class = FlightSerializer

    def post(self, request, *args, **kwargs):
        """
        works 24.03 16:39
        Create a new flight. 
        """
        return self.create(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        """
        works 24.03 16:31
        List of all flights.
        """
        return self.list(request, *args, **kwargs)
    


class FlightDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                     
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing an flight id.
    """
    logic = FlightLogic()
    queryset = logic.get_all()
    serializer_class = FlightSerializer

    def get(self, request, *args, **kwargs):
        """
        works 24.03 16:35
        Getting a specific flight.
        """
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        """
        works 24.03 16:37
        Updating a specific flight.
        """
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        """
        works 24.03 16:40
        Delete a specific flight.
        """
        return self.destroy(request, *args, **kwargs)