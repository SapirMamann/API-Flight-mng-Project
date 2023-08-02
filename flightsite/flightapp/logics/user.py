from ..dal.user import *


class UserLogic():
    dal = UserDal()

    def get_all(self):
        """
        Get all users
        """
        return self.dal.get_all() 



    def retrieve_by_username(self):
        pass
