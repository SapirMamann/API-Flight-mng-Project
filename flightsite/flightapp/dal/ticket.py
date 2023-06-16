from .base import BaseDAL
from ..models import *


class TicketDal(BaseDAL):
    def __init__(self):     #is this neccassary?
        super().__init__()


    def create(self, ticketname, password, email, role):
        """
        im using mixins so i dont need this 
        """
        pass


    def get_all(self):
        return Ticket.objects.all()
    

    def get_by_id(self, airline_id):
        pass


    def update_by_id(self, airline_id: int, data): 
        pass

    
    def delete():
        pass
    

