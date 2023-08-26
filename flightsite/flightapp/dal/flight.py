from .base import BaseDAL
from ..models import Flight
from .country import CountryDal


class FlightDal(BaseDAL):
    def __init__(self): 
        super().__init__()

    
    def get_all(self):
        return Flight.objects.all()
    

    def get_by_id(self, id):
        return Flight.objects.get(id=id)

    
    def get_by_airline_field(self, airline_company):
        return Flight.objects.filter(airline_company=airline_company)
    

    def get_by_params(self, origin_country):
        return Flight.objects.filter(origin_country=origin_country)
    

    def get_by_origin_country(self, origin_country):
        country_dal = CountryDal()
        # Get the country object
        country = country_dal.get_by_name(origin_country)
        if country is not None:
            # print(country, "country")
            country_id = country.id        #In order to use the filter method, i need to pass the country ID.
            return Flight.objects.all().filter(origin_country=country_id)
        else:
            return None
        

    def decrease_remaining_tickets(self, flight_id):
        flight = Flight.objects.get(id=flight_id)
        flight.remaining_tickets -= 1
        flight.save()
        return flight