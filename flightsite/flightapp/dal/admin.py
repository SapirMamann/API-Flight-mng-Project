from .base import BaseDAL
from ..models import Administrator


class AdminDal(BaseDAL):
    def __init__(self): #necessary?
        super().__init__()

    
    def get_all(self):
        return Administrator.objects.all()


