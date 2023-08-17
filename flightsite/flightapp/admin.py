from django.contrib import admin

from .models import (Country, Customer, 
    Administrator, AirlineCompany, Flight, Ticket)


admin.site.register(Country)
admin.site.register(Customer)
admin.site.register(Administrator)
admin.site.register(AirlineCompany)
admin.site.register(Flight)
admin.site.register(Ticket)
