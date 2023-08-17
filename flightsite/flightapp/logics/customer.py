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