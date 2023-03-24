from ..dal.admin import AdminDal 


class AdminLogic():
    dal = AdminDal()

    def get_all(self):
        """
        Get all users
        """
        return self.dal.get_all()


    def get_by_username(self, airline_username):
        """
        Get airline by username
        for login purposes,
        by entering username we'll get the airline
        """
        pass

