from .base import BaseDAL
from ..models import Customer


class CustomerDal(BaseDAL):
    def __init__(self): 
        super().__init__()

    
    def get_all(self):
        return Customer.objects.all()