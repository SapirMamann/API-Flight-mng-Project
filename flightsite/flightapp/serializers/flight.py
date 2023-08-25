from rest_framework import serializers
from django.utils import timezone
import dateutil.parser
from datetime import datetime, timezone

from ..models import Flight
from .country import CountrySerializer
from .airline import AirlineCompanySerializer
from .country import CountrySerializer

class FlightSerializer(serializers.ModelSerializer):
    # TODO: add validation of origin country differenr from destination country
    # add catch errors(when date is illigal)
        # validation no past flights
        
    # airline_company = AirlineCompanySerializer()
    # origin_country = CountrySerializer()
    # destination_country = CountrySerializer()


    class Meta:
        model = Flight
        fields = '__all__'


    # Validate origin and destination country is not the same
    def validate(self, attrs):
        if attrs['destination_country'] == attrs['origin_country']:
            raise serializers.ValidationError("Destination country and origin country must be different.")
        print(attrs)
        return attrs
    

    def validate_origin_country(self, value):
        if not value:
            raise serializers.ValidationError("Origin country cannot be empty.")
        return value


    def validate_destination_country(self, value):
        if not value:        
            raise serializers.ValidationError("Destination country cannot be empty.")
        return value


    def validate_departure_time(self, value):
        landing_time_str = self.initial_data.get('landing_time', None)
        print(landing_time_str)
        if landing_time_str is not None:
            landing_time = dateutil.parser.parse(landing_time_str)
            # make value and landing_time timezone-aware with UTC
            value = value.replace(tzinfo=timezone.utc)
            landing_time = landing_time.replace(tzinfo=timezone.utc)
            if value > landing_time:
                raise serializers.ValidationError("Departure time cannot be after landing time.")
        if value < datetime.now(timezone.utc):
            raise serializers.ValidationError("Departure time cannot be in the past.")
        return value


    def validate_remaining_tickets(self, value):
        """
        Check if there are enough remaining tickets to book.
        Cant have a negative amount of tickets.
        """
        if value <= 0:
            raise serializers.ValidationError("Flight's tickets must be a positive number.")        #i can raise a better error message
        return value
