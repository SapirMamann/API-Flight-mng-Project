from rest_framework import mixins, generics
from rest_framework.response import Response
from django.utils.decorators import method_decorator

from ..serializers.flight import FlightSerializer 
from ..logics.flight import FlightLogic
from ..logics.permission import user_permissions
from ..models import Flight

class FlightsList(generics.GenericAPIView, 
                  mixins.ListModelMixin, 
                  mixins.CreateModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = FlightLogic()
    queryset = logic.get_all()
    serializer_class = FlightSerializer

    @method_decorator(user_permissions('add_flight'))
    def post(self, request, *args, **kwargs):
        """
        Create a new flight. 
        """
        return self.create(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        """
        this should be allow any beacuse anonymous user can access this too
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

    @method_decorator(user_permissions('view_flight'))
    def get(self, request, *args, **kwargs):
        """
        Getting a specific flight.
        """
        return self.retrieve(request, *args, **kwargs)


    @method_decorator(user_permissions('change_flight'))
    def put(self, request, *args, **kwargs ):
        """
        Updating a specific flight.
        """
        flight = Flight.objects.get(id=kwargs['pk'])

        # Check if the request is for updating the flight details
        if 'destination_country' in request.data:
            print(request.data)
            return self.update(request, *args, **kwargs)

        # Check if the flight has remaining tickets
        if flight.remaining_tickets <= 0:
            return Response("Ticket error", status=404)
        else:
            flight.remaining_tickets -= 1
            flight.save()
            return Response({'status': 'success'})
    

    @method_decorator(user_permissions('delete_flight'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific flight.
        """
        return self.destroy(request, *args, **kwargs)
    