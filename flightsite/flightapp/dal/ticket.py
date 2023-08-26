from .base import BaseDAL
from ..models import *


class TicketDal(BaseDAL):
    def __init__(self):    
        super().__init__()


    def get_all(self):
        return Ticket.objects.all()
    

    def get_by_id(self, id):
        try:
            return Ticket.objects.get(id=id)
        except Ticket.DoesNotExist:
            return None
    

    def get_by_user(self, user_id):  
        return Ticket.objects.filter(user=user_id)
    
