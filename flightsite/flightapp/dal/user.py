from .base import BaseDAL
from ..models import *


class UserDal(BaseDAL):
    def __init__(self):     #is this neccassary?
        super().__init__()


    def create(self, username, password, email, role):
        pass


    def get_all(self):
        return User.objects.all()
    

    def get_by_id(self, airline_id):
        pass


    def update_by_id(self, airline_id: int, data): 
        pass

    
    def delete():
        pass