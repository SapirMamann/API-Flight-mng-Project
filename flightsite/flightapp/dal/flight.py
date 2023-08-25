from .base import BaseDAL
from ..models import Flight


class FlightDal(BaseDAL):
    def __init__(self): 
        super().__init__()

    
    def get_all(self):
        return Flight.objects.all()
    

    def get_by_id(self, id):
        return Flight.objects.get(id=id)
    
    
    def get_by_params(self, origin_country):
        return Flight.objects.filter(origin_country=origin_country)
    

    def decrease_remaining_tickets(self, flight_id):
        flight = Flight.objects.get(id=flight_id)
        flight.remaining_tickets -= 1
        flight.save()
        return flight