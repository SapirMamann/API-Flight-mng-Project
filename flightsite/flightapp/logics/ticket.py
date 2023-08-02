from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from ..dal.ticket import TicketDal
from ..dal.flight import FlightDal
from ..models import Flight


class TicketLogic():
    dal = TicketDal()

    def get_all(self):
        """
        Get all ticket roles
        """
        return self.dal.get_all() 


    def get_by_customer(self, user_id):
        pass
    #get all tickets of a specific customer
    
    
    def create_ticket_with_flight_update(self, data):
        """
        Create a ticket and update the flight remaining tickets
        """
        flight_dal = FlightDal()
        
        # logger
        flight = get_object_or_404(Flight, id=data['flight_no'])
        # print(flight)
        # print("this", flight.remaining_tickets)
        
        if flight.remaining_tickets <= 0:
            # Booking not successful, return a failure response
            print("not booked", flight.remaining_tickets)
            # return false 
            return Response({"message": "Booking failed. No remaining tickets available."},
                        status=status.HTTP_400_BAD_REQUEST)        
        else: 
            flight.remaining_tickets -=1
            print("booked with -1")
            flight.save()
            return Response({"message": "Booking successful."},
                        status=status.HTTP_201_CREATED)
        # log this after: <<<<<<<<<<
        # print("after",flight.remaining_tickets)