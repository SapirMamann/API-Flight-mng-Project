from ..dal.flight import FlightDal


class FlightLogic():
    dal = FlightDal()

    def get_all(self):
        """
        Get all flights
        """
        return self.dal.get_all() 
