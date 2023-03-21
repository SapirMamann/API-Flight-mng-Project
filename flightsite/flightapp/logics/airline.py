from ..models import *
from ..dal.airline import AirlineDal


class AirlineLogic():
    def get_by_id(self, airline_id):
        dal = AirlineDal()
        return dal.get_by_id(airline_id)


    def create(self, user_id, name, country_id):
        return AirlineDal.create(self, user_id, name, country_id)
        
        
