from .base import BaseDAL
from ..models import Country


class CountryDal(BaseDAL):
    def __init__(self): #is this neccassary?
        super().__init__()


    def get_all(self):
        return Country.objects.all()
