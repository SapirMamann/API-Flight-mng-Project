from rest_framework import serializers

from ..models import Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


    # def validate_destination_country(self, origin_country, destination_country):
    #     if destination_country == origin_country:
    #         raise serializers.ValidationError('Destination country and origin country must be different')
    #     return True
    

    # def validate_departure_time(self, time):
    #     """
    #     i might have to import  time for this validator
    #     Departure time cant be in the past
    #     """


    # def validate_landing_time(self, time):
    #     """
    #     Landing time cant be earlier than departure time
    #     """


    def validate_remaining_tickets(self, value):
        """
        Cant have a negative amount of tickets
        """
        if int(value) < 0:
            raise serializers.ValidationError("Flight's tickets must be a positive number.")        #i can raise a better error message
        return value
