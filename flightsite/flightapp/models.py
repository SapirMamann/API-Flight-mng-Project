from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        permissions = [
            ("can_view_countries", "Can view countries")
        ]

    def __str__(self):
        return self.name


# class UserRoles(models.Model):
#     role = models.CharField(max_length=30, unique=True)

#     def __str__(self):
#         return self.role


class UserGroup(Group):
    # my_permissions = models.ManyToManyField(Permission, verbose_name='my_permissions', blank=True)

    class Meta:
        proxy = True        #UserGroup doesn't create a new database table, but instead creates a new Python class that represents Group.

    # @property
    # def group_permissions(self):
    #     perms = super().permissions
    #     # modify the list of permissions based on the group name
    #     if self.name == 'Administrator':        #group no 1
    #         perms.add('can_add_user')
    #     elif self.name == 'Airline company':        #group no 2
    #         pass
    #     elif self.name == 'Customer':       #group no 3
    #         pass
    #     return perms


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.TextField(max_length=250)
    email = models.EmailField(max_length=30, unique=True)
    user_role = models.ForeignKey(UserGroup, on_delete=models.CASCADE, default='1', related_name='user_role')

    # class Meta:
    #     permissions = [
    #         ("view_user_test", "view user test"),
    #     ]

    def __str__(self):
        return self.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, unique=True)
    credit_card = models.CharField(max_length=30)

    class Meta:
        permissions = [
            ('add_ticket', 'can book a flight'),
        ]

    def __str__(self):
        return self.first_name
    

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        permissions = [
            ('add_country',"can add a country"),
        ]
    

class AirlineCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Flight(models.Model):
    airline_company = models.ForeignKey(AirlineCompany, 
                                        on_delete=models.CASCADE, default='unknown')
    origin_country = models.ForeignKey(Country, related_name='departures', 
                                       on_delete=models.CASCADE, default='unknown')
    destination_country = models.ForeignKey(Country, related_name='arrivals', 
                                            on_delete=models.CASCADE, default='unknown')
    departure_time = models.DateTimeField()
    landing_time = models.DateTimeField()
    remaining_tickets = models.IntegerField()

    def __str__(self):
        return f'{self.origin_country}-{self.destination_country}'


class Ticket(models.Model):
    flight_no = models.ForeignKey(Flight, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)