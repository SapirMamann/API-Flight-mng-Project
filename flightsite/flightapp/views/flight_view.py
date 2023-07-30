from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework import mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ..serializers.flight import FlightSerializer 
from ..logics.flight import FlightLogic
from ..logics.permission import user_permissions
from ..models import Flight, Country, User
from .ticket_view import TicketsList
import requests


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
        This should be allow any (without permission decorator) beacuse anonymous user can access this too
        List of all flights.
        """
        return self.list(request, *args, **kwargs)
    


class FlightsByCountry(APIView):
    """
    For displaying flights based on their origin_country.
    """
    permission_classes = [AllowAny]

    def get(self, request, country):
        country = get_object_or_404(Country, name=country)
        country = country.id        #In order to use the filter method, i need to pass the country ID.

        queryset = Flight.objects.all().filter(origin_country=country)
        serializer = FlightSerializer(queryset, many=True)
        return Response(serializer.data)



class FlightDetail(generics.GenericAPIView,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,                     
                   mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing a flight id.
    """
    logic = FlightLogic()
    queryset = logic.get_all()
    serializer_class = FlightSerializer

    # @method_decorator(user_permissions('view_flight'))
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
        return self.update(request, *args, **kwargs)


    @method_decorator(user_permissions('delete_flight'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific flight.
        """
        return self.destroy(request, *args, **kwargs)
    


class BookFlight(APIView):
    def get(self, request, flight_id):
        """
        Create a new ticket for a user that booked a flight.
        """
        # Check if flight exists by its id
        flight = get_object_or_404(Flight, id=flight_id)
        print(flight) #str
        print(flight_id) #id
        # print(request.user)
        # print(request.user.id)

        #Get user details
        user = get_object_or_404(User, id=request.user.id)
        print(user)
        # create a ticket instance
        data = {
            'flight_no': flight_id,
            'user': request.user.id
        }
        # response = TicketsList.post(self, request, data=data)
        # response = TicketsList.post(self, request, 'flight_no: flight_id')
        # response = self.create(request, data)
        # r = requests.post('http://127.0.0.1:8000/api/tickets/', params=data)



        # print(r)
        # tickets_list_view = TicketsList.as_view()  # Create an instance of TicketsList view
        # print(tickets_list_view(request, *args, **kwargs))  # Call the post method of TicketsList view
        # response = tickets_list_view(request, *args, **kwargs)  # Call the post method of TicketsList view

        return Response(status=200)

        # # check if there are enough tickets in this flight
        # if flight.remaining_tickets <= 0:
        #     return Response({'message': 'No remaining tickets'}, status=status.HTTP_400_BAD_REQUEST)
        
        # #send a form to complete user's data

        # # check if user filled his details
        # if not user.first_name or not user.last_name or not user.email:
        #     return Response({'message': 'User details incomplete'}, status=status.HTTP_400_BAD_REQUEST)

        # # create a new ticket in the db
        # # view = TicketsList.as_view()
        # # serializer = TicketSerializer(data={'flight_no': flight.id, 'user': user.id})
        # # if serializer.is_valid():
        # #     ticket = view(request=request, serializer=serializer).post(request)
            
        #     #decrease the number of tickets by one
        # flight.remaining_tickets -= 1
        # flight.save()
            
        # return Response({'message': 'Ticket booked successfully'})
        # # else:
        # #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchFlight(APIView):
    def get(self, request, *args, **kwargs):
        # Getting params from client(react)
        origin_country = request.GET.get('origin_country')

        logic = FlightLogic()
        flights = logic.get_by_params(origin_country)
        
        serializer = FlightSerializer(flights, many=True)
        serialized_flights = serializer.data

        print("ok", flights)

        context = {'flights': serialized_flights}
        return Response({'flights': serialized_flights})
