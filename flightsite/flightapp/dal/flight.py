from .base import BaseDAL
from ..models import Flight


class FlightDal(BaseDAL):
    def __init__(self): 
        super().__init__()

    
    def get_all(self):
        return Flight.objects.all()
    

    def get_by_params(self, origin_country):
        return Flight.objects.filter(origin_country=origin_country)