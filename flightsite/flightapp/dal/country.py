from django.shortcuts import get_object_or_404

from .base import BaseDAL
from ..models import Country


class CountryDal(BaseDAL):
    def __init__(self): 
        super().__init__()


    def get_all(self):
        return Country.objects.all()


    def get_by_name(self, name):
        try:
            return Country.objects.get(name=name)
        except Country.DoesNotExist:
            return None