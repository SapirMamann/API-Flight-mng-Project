from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from datetime import datetime

from ..serializers.flight import FlightSerializer 
from ..logics.flight import FlightLogic
from ..logics.permission import user_permissions
from ..models import Flight, Country, User, AirlineCompany
from .ticket_view import TicketsList


class FlightsList(generics.GenericAPIView, 
                  mixins.ListModelMixin, 
                  mixins.CreateModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = FlightLogic()
    queryset = logic.get_all()
    serializer_class = FlightSerializer

    @method_decorator(user_permissions('flightapp.add_flight'))
    def post(self, request, *args, **kwargs):
        """
        Create a new flight. 
        """
        print(request.data)
        return self.create(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        """
        This should be allow any (without permission decorator) beacuse anonymous user can access this too
        List of all flights.
        """
        return self.list(request, *args, **kwargs)



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

    # @method_decorator(user_permissions('flightapp.view_flight'))
    def get(self, request, *args, **kwargs):
        """
        Getting a specific flight.
        maybe permission allow any
        """
        return self.retrieve(request, *args, **kwargs)


    @method_decorator(user_permissions('flightapp.change_flight'))
    def put(self, request, *args, **kwargs ):
        """
        Updating a specific flight.
        """
        return self.update(request, *args, **kwargs)


    @method_decorator(user_permissions('flightapp.delete_flight'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific flight.
        """
        return self.destroy(request, *args, **kwargs)



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
    


class SearchFlight(APIView):
    def get(self, request, *args, **kwargs):
        # Getting params from client(react)
        # origin_country = request.GET.get('origin_country')

        # logic = FlightLogic()
        # # flights = logic.get_by_params(origin_country)
        
        # serializer = FlightSerializer(flights, many=True)
        # serialized_flights = serializer.data

        # print("ok", flights)
        # context = {'flights': serialized_flights}
        # return Response({'flights': serialized_flights})
        try:
            origin_country_id = request.GET.get("origin_country")
            destination_country_id = request.GET.get("destination_country")
            departure_time = request.GET.get("departure_time")

            # Create a base queryset for filtering flights
            queryset = Flight.objects.all()
            
            # Apply filters based on query parameters
            if origin_country_id:
                queryset = queryset.filter(origin_country=origin_country_id)
            
            if destination_country_id:
                queryset = queryset.filter(destination_country=destination_country_id)
            
            if departure_time:
                print(departure_time, "d tmie")
                # departure_time = datetime.strptime(departure_time, "%Y-%m-%dT%H:%M:%S%z")
                formatted_date = datetime.fromisoformat(departure_time)

                queryset = queryset.filter(departure_time=formatted_date)
            
            # Serialize the filtered flights
            serializer = FlightSerializer(queryset, many=True)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class AirlineCompanyFlights(APIView):
    """
    For displaying flights of the logged-in airline company.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        # Get the airline comapny object based on the requested user id
        airline_company_instance = AirlineCompany.objects.get(user=user_id)
        print(airline_company_instance)

        queryset = Flight.objects.filter(airline_company=airline_company_instance)
        serializer = FlightSerializer(queryset, many=True)
        return Response(serializer.data)
