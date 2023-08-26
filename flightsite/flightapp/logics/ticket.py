from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from ..dal.ticket import TicketDal
from ..dal.flight import FlightDal
from ..models import Flight
from .flight import FlightLogic
from ..serializers.ticket import TicketSerializer


class TicketLogic():
    dal = TicketDal()

    def get_all(self):
        """
        Get all ticket roles
        """
        return self.dal.get_all() 


    def get_by_user(self, user_id):
        #get all tickets of a specific user
        user_tickets = self.dal.get_by_user(user_id)
        if user_tickets:
            serializer = TicketSerializer(user_tickets, many=True)
            return serializer.data
        else:
            return None
        

    def get_by_id(self, id):
        """
        Get a specific ticket by id
        """
        return self.dal.get_by_id(id)
    
    
    def create_ticket_with_flight_update(self, data):
        """
        Create a ticket and update the flight remaining tickets
        """
        flight_dal = FlightDal()
        
        # logger
        flight = get_object_or_404(Flight, id=data['flight_no'])
        print(flight)
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


    def delete_ticket_with_flight_update(self, ticket_id):
        """
        Delete a ticket and update the flight remaining tickets by one
        """
        try:
            # Get ticket by id
            ticket = self.dal.get_by_id(ticket_id)
            # Get flight id from ticket
            flight_id = ticket.flight_no.id

            # Get flight by id
            flight_logic = FlightLogic()
            flight_instance = flight_logic.get_flight_by_id(flight_id)

            # Add ticket amount by one
            flight_instance.remaining_tickets += 1
            flight_instance.save()      
        except Exception as e:
            print("An error occurred:", e)