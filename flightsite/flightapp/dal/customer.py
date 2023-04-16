from .base import BaseDAL
from ..models import Customer

class CustomerDal(BaseDAL):
    def __init__(self): #is this neccassary?
        super().__init__()

    
    def create(self, user_id, first_name, last_name, address, phone, credit_card):
        pass

    def get_all(self):
        return Customer.objects.all()
    
    
    def get_by_id(self):
        pass


    def update_by_id(self): 
        pass

    
    def delete(self):
        pass
