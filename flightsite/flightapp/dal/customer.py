from .base import BaseDAL
from ..models import Customer

class CustomerDal(BaseDAL):
    def __init__(self): #is this neccassary?
        super().__init__()

    
    def create(self, user_id, first_name, last_name, address, phone, credit_card):
        return Customer.objects.create(
            user=user_id,
            first_name=first_name, 
            last_name=last_name,
            address=address, 
            phone=phone,
            credit_card=credit_card)


    def get_by_id(self):
        pass


    def update_by_id(self): 
        pass

    
    def delete(self):
        pass
