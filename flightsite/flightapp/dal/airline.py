from .base import BaseDAL
from ..models import AirlineCompany


class AirlineDal(BaseDAL):
    def __init__(self):     #is this neccassary?
        super().__init__()


    def get_all(self):
        return AirlineCompany.objects.all()
    