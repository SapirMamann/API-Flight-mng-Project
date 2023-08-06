from django.db import models
from django.contrib.auth.models import Group, User, PermissionsMixin


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name



# class UserGroup(Group):
#     class Meta:
#         proxy = True        #UserGroup doesn't create a new database table, but instead creates a new Python class that represents Group.



# class User(AbstractUser, PermissionsMixin):
#     username = models.CharField(max_length=50, unique=True)
#     password = models.TextField(max_length=250)
#     email = models.EmailField(max_length=30, unique=True)
#     user_role = models.ForeignKey(UserGroup, on_delete=models.CASCADE, default=None, related_name='user_role')

#     def __str__(self):
#         return self.username



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, unique=True)
    credit_card = models.CharField(max_length=30)
    
    #user is assigned to the group only when the instance is being created
    def save(self, *args, **kwargs):
        created = not bool(self.pk)
        super().save(*args, **kwargs)
        
        if created:
            # assign model to a group
            group = Group.objects.get(name='Customer')
            self.user.groups.add(group)

    def __str__(self):
        return self.first_name
    


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    #user is assigned to the group only when the instance is being created
    def save(self, *args, **kwargs):
        created = not bool(self.pk)
        super().save(*args, **kwargs)
        
        if created:
            # assign model to a group
            group = Group.objects.get(name='Administrator')
            self.user.groups.add(group)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    


class AirlineCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    #user is assigned to the group only when the instance is being created
    def save(self, *args, **kwargs):
        created = not bool(self.pk)
        super().save(*args, **kwargs)
        
        if created:
            # assign model to a group
            group = Group.objects.get(name='Airline company')
            self.user.groups.add(group)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flight_no}, {self.user}'