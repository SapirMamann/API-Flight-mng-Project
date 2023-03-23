from .base import BaseDAL
from ..models import *


class AirlineDal(BaseDAL):
    def __init__(self):     #is this neccassary?
        super().__init__()


    def create(self, user_id, name, country_id):
        user = User.objects.get(id=user_id)
        country = Country.objects.get(id=country_id)

        new_airline = AirlineCompany.objects.create(
            user=user,
            name=name,
            country=country)
        
        return new_airline


    def get_all(self):
        return AirlineCompany.objects.all()
    

    def get_by_id(self, airline_id):
        return AirlineCompany.objects.get(id=airline_id) 


    def update_by_id(self, airline_id: int, data): 
        airline = AirlineCompany.objects.get(id=airline_id)

        airline.name = data['name']
        airline.user = User.objects.get(id=data['user_id'])
        airline.country = Country.objects.get(id=data['country_id'])
        airline.save()
        #add logging

    
    def delete():
        pass
    