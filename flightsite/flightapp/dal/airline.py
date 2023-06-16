from .base import BaseDAL
from ..models import AirlineCompany


class AirlineDal(BaseDAL):
    def __init__(self):     #is this neccassary?
        super().__init__()


    def create(self, user_id, name, country_id):
        pass

    def get_all(self):
        return AirlineCompany.objects.all()
    

    def get_by_id(self, airline_id):
        pass

    def update_by_id(self): 
        pass
    
    def delete():
        pass
