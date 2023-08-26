from .base import BaseDAL
from ..models import Administrator


class AdminDal(BaseDAL):
    def __init__(self): #necessary?
        super().__init__()

    
    def get_all(self):
        return Administrator.objects.all()
    

    def get_by_user_field(self, user):
        return Administrator.objects.filter(user=user).first()

           

