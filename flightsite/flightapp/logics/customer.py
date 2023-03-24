from ..dal.customer import CustomerDal


class CustomerLogic():
    dal = CustomerDal()

    def get_all(self):
        """
        Get all customers
        """
        return self.dal.get_all() 


    # def get_by_id(self, user_id):
    #     """
    #     Get customer by customer ID
    #     """
    #     return self.dal.get_by_id(user_id)


    # def get_by_username(self, customer_username):
    #     """
    #     Get customer by username
    #     for login purposes,
    #     by entering username we'll get the customer
    #     """
    #     pass