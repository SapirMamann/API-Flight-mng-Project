from datetime import datetime
from rest_framework import mixins, generics, status
from rest_framework.response import Response

from ..dal.airline import AirlineDal
from ..dal.flight import FlightDal
from ..serializers.flight import FlightSerializer


class FlightLogic():
    dal = FlightDal()

    def get_all(self):
        """
        Get all flights
        """
        return self.dal.get_all() 


    def get_flight_by_id(self, id):
        """
        Get a specific flight by id
        """
        return self.dal.get_by_id(id)


    def get_by_country(self, country):
        queryset = self.dal.get_by_origin_country(country)
        serializer = FlightSerializer(queryset, many=True)
        return serializer.data
    

    def get_by_params(self, origin_country_id, destination_country_id, departure_time):
        # Get all flights, then create a base queryset for filtering flights
        queryset = self.dal.get_all()
        
        # Apply filters based on query parameters
        if origin_country_id:
            queryset = queryset.filter(origin_country=origin_country_id)
        
        if destination_country_id:
            queryset = queryset.filter(destination_country=destination_country_id)
        
        if departure_time:
            # Parse the departure_time string into a datetime object
            formatted_date = datetime.fromisoformat(departure_time)
            
            # Calculate the start and end of the day for the given departure_time
            start_of_day = formatted_date.replace(hour=0, minute=0, second=0)
            end_of_day = formatted_date.replace(hour=23, minute=59, second=59)

            # Filter flights within the specified day
            queryset = queryset.filter(departure_time__range=(start_of_day, end_of_day))
            print(queryset)
        # Serialize the filtered flights
        serializer = FlightSerializer(queryset, many=True)
        # print(serializer.data, "serialized fligth search")
        return serializer.data


    def get_by_airline(self, airline_company_user_id):
        """
        Get all flights of a specific airline company,
        based on the request.user.id.
        """
        airline_dal = AirlineDal()
        # Get the airline comapny object based on the requested user id
        # So i can filter fligths based on the airline company field
        # send user to get_by_user_field airline dal 
        airline_company_instance = airline_dal.get_by_user_field(airline_company_user_id)
        # print(airline_company_instance, "airline company instance")
        # Get all flights of the airline company
        queryset = self.dal.get_by_airline_field(airline_company_instance)

        serializer = FlightSerializer(queryset, many=True)
        return serializer.data


    def get_arrival_flights(self, destination_country):
        pass
    #that lands in the given country


    def get_departure_flights(self, origin_country):
        pass
    #that take off from the given country


