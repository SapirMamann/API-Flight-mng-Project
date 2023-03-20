from ..models import *
from ..dal.airline import AirlineDal


class AirlineLogic():
    def get_by_id(self, airline_id):
        airline = AirlineCompany.objects.get(id=airline_id)
        return airline


    def create(self, user_id, name, country_id):
        return AirlineDal.create(self, user_id, name, country_id)
        
        
