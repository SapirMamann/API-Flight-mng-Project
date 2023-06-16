from .base import BaseDAL
from ..models import Country


class CountryDal(BaseDAL):
    def __init__(self): #is this neccassary?
        super().__init__()

    
    def create(self, country_id, first_name, last_name, address, phone, credit_card):
        pass
        

    def get_all(self):
        return Country.objects.all()
    

    def get_by_id(self):
        pass


    def update_by_id(self): 
        pass

    
    def delete(self):
        """
        Delete country role
        """
        pass
