from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..logics.ticket import TicketLogic
from ..serializers.ticket import TicketSerializer
from ..models import Flight


class TicketsList(generics.GenericAPIView, 
                    mixins.ListModelMixin, 
                    mixins.CreateModelMixin):
    """
    Handles POST and GET requests
    """
    logic = TicketLogic()
    queryset = logic.get_all()
    serializer_class = TicketSerializer

    def post(self, request, *args, **kwargs):
        """
        works 25.03 12:15
        Add ticket. 
        """
        return self.create(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        """
        works 25.03 12:10
        List of all countries.
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

    def get(self, request, *args, **kwargs):
        """
        works 25.03 12:17
        Getting a specific ticket.
        """
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        """
        works 25.03 12:15
        Updating a specific ticket.
        """
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        """
        works 25.03 12:22
        Delete a specific ticket.
        """
        return self.destroy(request, *args, **kwargs)
