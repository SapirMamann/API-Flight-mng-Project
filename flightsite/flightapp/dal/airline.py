from .base import BaseDAL
from ..models import AirlineCompany


class AirlineDal(BaseDAL):
    def __init__(self):   
        super().__init__()


    def get_all(self):
        return AirlineCompany.objects.all()
    

    def get_by_user_field(self, user_id):
        return AirlineCompany.objects.filter(user=user_id).first()