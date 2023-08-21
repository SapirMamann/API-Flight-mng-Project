from rest_framework import serializers
from django.utils import timezone
import dateutil.parser

from ..models import Flight
from .country import CountrySerializer

from datetime import datetime, timezone

class FlightSerializer(serializers.ModelSerializer):
    # TODO: add validation of origin country differenr from destination country
    # add catch errors(when date is illigal)
        # validation no past flights
    # In order to get the name field of a foreign key and not the pk. 
    # airline_company = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # origin_country = serializers.SlugRelatedField(slug_field="name", read_only=True)
    # destination_country = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Flight
        fields = '__all__'


    # def validate(self, ):
    # pass

    def validate_destination_country(self, destination_country):
        origin_country = self.initial_data.get('origin_country')

        if str(destination_country.id) == origin_country:
            raise serializers.ValidationError('Destination country and origin country must be different.')
        return destination_country
    

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
