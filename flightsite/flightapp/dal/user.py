from .base import BaseDAL
from ..models import *


class UserDal(BaseDAL):
    def __init__(self):     
        super().__init__()


    def get_all(self):
        return User.objects.all()
    
