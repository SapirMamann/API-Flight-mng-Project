from .base import BaseDAL
from ..models import Flight


class FlightDal(BaseDAL):
    def __init__(self): 
        super().__init__()

    
    def get_all(self):
        return Flight.objects.all()
    
