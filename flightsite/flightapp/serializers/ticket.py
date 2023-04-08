from rest_framework import serializers

from ..models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

#validate that the given flight has enough remaining tickets for the customer to book a ticket.