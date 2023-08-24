from rest_framework import serializers

from ..models import Ticket
from .flight import FlightSerializer

class TicketSerializer(serializers.ModelSerializer):
    flight_no = FlightSerializer()


    class Meta:
        model = Ticket
        fields = '__all__'


    #validate that the given flight has enough remaining tickets for the customer to book a ticket.
    def validate_remaining_tickets(self, remaining_tickets):
        if remaining_tickets < 0:
            raise serializers.ValidationError('Remaining tickets cant be negative.')
        return remaining_tickets
    