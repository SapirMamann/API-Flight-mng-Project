from ..dal.ticket import TicketDal
from ..models import Flight

class TicketLogic():
    dal = TicketDal()

    def get_all(self):
        """
        Get all ticket roles
        """
        return self.dal.get_all() 


    def buy_ticket(self, flight_no):
        """
        Decrease the amount of tickets by one
        """
        # get ticket left amount and decrease by one
        # tickets_left = 
        # print (tickets_left)
        