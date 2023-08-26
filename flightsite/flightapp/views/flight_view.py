from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..serializers.flight import FlightSerializer 
from ..logics.flight import FlightLogic
from ..logics.permission import user_permissions
from ..models import Flight, Country, User, AirlineCompany


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
    logic = FlightLogic()

    def get(self, request, country):
        response = self.logic.get_by_country(country)
        return Response(response)
    


class SearchFlight(APIView):
    logic = FlightLogic()

    def get(self, request, *args, **kwargs):
        try:
            origin_country_id = request.GET.get("origin_country")
            destination_country_id = request.GET.get("destination_country")
            departure_time = request.GET.get("departure_time")

            response = self.logic.get_by_params(origin_country_id, destination_country_id, departure_time)
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class AirlineCompanyFlights(APIView):
    """
    For displaying flights of the logged-in airline company.
    """
    permission_classes = [IsAuthenticated]
    logic = FlightLogic()

    def get(self, request):
        airline_user_id = request.user.id
        response = self.logic.get_by_airline(airline_user_id)
        # print(response, "response")
        return Response(response, status=status.HTTP_200_OK)
