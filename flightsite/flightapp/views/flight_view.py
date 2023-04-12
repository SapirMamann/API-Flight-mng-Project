from rest_framework import mixins, generics
from rest_framework.views import Response
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin

from ..serializers.flight import FlightSerializer 
from ..logics.flight import FlightLogic
from ..models import Flight


from django.utils.decorators import method_decorator
from ..logics.permission import user_permissions

class FlightsList(generics.GenericAPIView, 
                  PermissionRequiredMixin,
                  mixins.ListModelMixin, 
                  mixins.CreateModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = FlightLogic()
    queryset = logic.get_all()
    serializer_class = FlightSerializer
    permission_required = 'add_flight'

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


    def put(self, request, pk):
        """
        works 24.03 16:37
        Updating a specific flight.
        """
        
        flight = Flight.objects.get(id=pk)
        flight.remaining_tickets -= 1
        flight.save()
        return Response({'status': 'success'})

    

    def delete(self, request, *args, **kwargs):
        """
        works 24.03 16:40
        Delete a specific flight.
        """
        return self.destroy(request, *args, **kwargs)
    
# @api_view(['PUT'])  
# def reserve_seat(flight_no):
#     try:
#         flight = Flight.objects.get(id=flight_no)
#         flight.remaining_tickets -= 1
#         flight.save()
#         return Response({'status': 'success'})
    
#     except Flight.DoesNotExist:
#         return Response({'status': 'error', 'message': f'Flight {flight_no} not found'})

