from ..dal.customer import CustomerDal


class CustomerLogic():
    dal = CustomerDal()

    def get_all(self):
        """
        Get all customers
        """
        return self.dal.get_all() 

