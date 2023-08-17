from .base import BaseDAL
from ..models import Customer
from django.contrib.auth.models import User
from rest_framework.response import Response

class CustomerDal(BaseDAL):
    def __init__(self): 
        super().__init__()

    
    def get_all(self):
        return Customer.objects.all()
    

    def get_customer_by_user_username(self, username):
        try:
            # Get the user based on the username
            user = User.objects.get(username=username)
            return user
            # Get the customer by its user field
            # customer = Customer.objects.get(user=user)
            # if customer is not None:
            #     return customer
            # else:
            #     return Response({'error': 'Customer not found'}, status=404)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)