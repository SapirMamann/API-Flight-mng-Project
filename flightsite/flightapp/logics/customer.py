from ..dal.customer import CustomerDal


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
    

    def delete_customer_with_user(self, customer_instance):
        user_instance = customer_instance.user

        # Delete the customer instance
        customer_instance.delete()

        # Delete the user instance
        user_instance.delete()