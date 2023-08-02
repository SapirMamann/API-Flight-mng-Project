from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..logics.ticket import TicketLogic
from ..serializers.ticket import TicketSerializer
from ..logics.permission import user_permissions
from ..models import Flight, Country, User


class TicketsList(
                  mixins.ListModelMixin, 
                  mixins.CreateModelMixin, generics.GenericAPIView):
    """
    Handles POST and GET requests
    """
    logic = TicketLogic()
    queryset = logic.get_all()
    serializer_class = TicketSerializer

    @method_decorator(user_permissions('add_ticket'))
    def post(self, request, *args, **kwargs):
        """
        Add ticket. 
        """
        # print(request.data)
        self.logic.create_ticket_with_flight_update(request.data)
        return self.create(request, *args, **kwargs)


    @method_decorator(user_permissions('view_ticket'))
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

    @method_decorator(user_permissions('view_ticket'))
    def get(self, request, *args, **kwargs):
        """
        Getting a specific ticket.
        """
        return self.retrieve(request, *args, **kwargs)


    @method_decorator(user_permissions('change_ticket'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific ticket.
        """
        return self.update(request, *args, **kwargs)
    

    @method_decorator(user_permissions('delete_ticket'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific ticket.
        """
        return self.destroy(request, *args, **kwargs)


