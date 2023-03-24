from .base import BaseDAL
from ..models import Administrator

class AdminDal(BaseDAL):
    def __init__(self): #is this neccassary?
        super().__init__()

    
    def create(self, user_id, first_name, last_name, address, phone, credit_card):
        pass


    def get_all(self):
        return Administrator.objects.all()


    def get_by_id(self):
        pass


    def update_by_id(self): 
        pass

    
    def delete(self):
        """
        Delete admin/ customer/ airline company/ flight/ ticket everything
        """
        pass
