from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..logics.ticket import TicketLogic
from ..logics.flight import FlightLogic
from ..serializers.ticket import TicketSerializer
from ..logics.permission import user_permissions


class TicketsList(mixins.ListModelMixin, 
                  mixins.CreateModelMixin, generics.GenericAPIView):
    """
    Handles POST and GET requests
    """
    logic = TicketLogic()
    queryset = logic.get_all()
    serializer_class = TicketSerializer

    @method_decorator(user_permissions('flightapp.add_ticket'))
    def post(self, request, *args, **kwargs):
        """
        Add ticket. 
        Is used for booking flight.
        """
        # print(request.data)
        # print("user", request.user.get_group_permissions())
        self.logic.create_ticket_with_flight_update(request.data)
        return self.create(request, *args, **kwargs)


    @method_decorator(user_permissions('flightapp.view_ticket'))
    def get(self, request, *args, **kwargs):
        """
        List of all tickets.
        """
        return self.list(request, *args, **kwargs)
    


class TicketDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                     
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing a ticket id.
    """
    logic = TicketLogic()
    queryset = logic.get_all()
    serializer_class = TicketSerializer

    @method_decorator(user_permissions('flightapp.view_ticket'))
    def get(self, request, *args, **kwargs):
        """
        Getting a specific ticket.
        """
        return self.retrieve(request, *args, **kwargs)


    @method_decorator(user_permissions('flightapp.change_ticket'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific ticket.
        """
        return self.update(request, *args, **kwargs)
    

    @method_decorator(user_permissions('flightapp.delete_ticket'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific ticket.
        """
        # Add ticket amount by one on specific flight
        # Get flight id from request
        ticket_id = kwargs['pk']
        self.logic.delete_ticket_with_flight_update(ticket_id)
        return self.destroy(request, *args, **kwargs)



class TicketsByUserID(APIView):
    """
    For getting tickets based on the logged in user.
    """
    permission_classes = [IsAuthenticated]
    logics = TicketLogic()
    serializer_class = TicketSerializer

    def get(self, request, pk):
        response = self.logics.get_by_user(pk)
        if response is None:
            return Response({"detail": "No tickets found for the user."}, status=status.HTTP_404_NOT_FOUND)
        # print(response, "response")
        return Response(response, status=status.HTTP_200_OK)
    