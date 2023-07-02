from ..dal.flight import FlightDal


class FlightLogic():
    dal = FlightDal()

    def get_all(self):
        """
        Get all flights
        """
        return self.dal.get_all() 


    def get_by_params(self, origin_country):
        return self.dal.get_by_params(origin_country)