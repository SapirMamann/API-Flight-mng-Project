from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from ..logics.ticket import TicketLogic
from ..serializers.ticket import TicketSerializer
from ..logics.permission import user_permissions


class TicketsList(
                  mixins.ListModelMixin, 
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
        print(request.data)
        print("user", request.user.get_group_permissions())
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
        return self.destroy(request, *args, **kwargs)



class TicketsByUserID(APIView):
    """
    For getting tickets based on the logged in user.
    """
    # permission_classes = is_authenticated
    logics = TicketLogic()
    serializer_class = TicketSerializer

    def get(self, request, pk):
        print(request.user, "request.user in TicketsByUserID")
        print(request.user.is_authenticated, "request.user in TicketsByUserID")
        # //maybe should be try except because i want to let admin search tickets by user id
        # should be is authenticated
        if request.user.is_authenticated:
            user_tickets = self.logics.get_by_user(pk)
            if user_tickets:
                serializer = TicketSerializer(user_tickets, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No tickets found for this user."},
                                status=status.HTTP_200_OK)