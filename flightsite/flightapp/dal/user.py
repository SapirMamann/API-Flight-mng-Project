from .base import BaseDAL
from django.contrib.auth.models import User


class UserDal(BaseDAL):
    def __init__(self):     
        super().__init__()


    def get_all(self):
        return User.objects.all()
    
    
    def get_by_id(self, id):
        try:
            return User.objects.get(id=id) 
        except User.DoesNotExist:
            return None