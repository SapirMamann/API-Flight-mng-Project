from ..dal.user import *


class UserLogic():
    dal = UserDal()

    def get_all(self):
        """
        Get all users
        """
        return self.dal.get_all() 


    def get_by_id(self, user_id):
        """
        Get user by ID
        """
        return self.dal.get_by_id(user_id)


    def create(self, user_id, name, country_id):
        """
        Create a new user- based on information provided by user
        """
        # return self.dal.create(user_id, name, country_id)
        
        
