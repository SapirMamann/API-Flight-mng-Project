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
    #needs to add destination and departure time


    def get_arrival_flights(self, destination_country):
        pass
    #that lands in the given country


    def get_departure_flights(self, origin_country):
        pass
    #that take off from the given country