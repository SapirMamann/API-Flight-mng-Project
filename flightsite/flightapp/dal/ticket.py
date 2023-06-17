from .base import BaseDAL
from ..models import *


class TicketDal(BaseDAL):
    def __init__(self):     #is this neccassary?
        super().__init__()


    def get_all(self):
        return Ticket.objects.all()
