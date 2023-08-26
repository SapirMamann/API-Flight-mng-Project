from rest_framework.response import Response

from ..dal.customer import CustomerDal
from ..dal.user import UserDal
from ..serializers.customer import CustomerSerializer


class CustomerLogic():
    dal = CustomerDal()

    def get_all(self):
        """
        Get all customers
        """
        return self.dal.get_all() 


    def get_customer_by_user_username(self, username):
        """
        Get customer by its user's username
        """
        return self.dal.get_customer_by_user_username(username)
    

    def get_by_user_id(self, user_id):
        """
        Get customer instance by user ID
        """
        user_dal = UserDal()
        try:
            user = user_dal.get_by_id(user_id)
            customer_instance = self.dal.get_by_user_field(user)
            if customer_instance:
                # print("customer_instance", customer_instance)
                serializer = CustomerSerializer(customer_instance)
                return Response(serializer.data)
            else:
                return Response({
                    'error': 'Customer not found'
                }, status=404)
        except Exception as e:
            return Response({
                'error': str(e) + 'User not found'
            }, status=404)
   

    def delete_customer_with_user(self, customer_instance):
        user_instance = customer_instance.user

        # Delete the customer instance
        customer_instance.delete()

        # Delete the user instance
        user_instance.delete()