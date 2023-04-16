from ..dal.ticket import TicketDal
from ..models import Flight

class TicketLogic():
    dal = TicketDal()

    def get_all(self):
        """
        Get all ticket roles
        """
        return self.dal.get_all() 

