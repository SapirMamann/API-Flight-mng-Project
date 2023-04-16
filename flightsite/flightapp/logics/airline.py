from ..dal.airline import AirlineDal


class AirlineLogic():
    dal = AirlineDal()

    def get_all(self):
        """
        Get all airline Companies
        """
        return self.dal.get_all() 


    def get_by_id(self, airline_id):
        """
        Get airline by airline ID
        """
        return self.dal.get_by_id(airline_id)


    def get_by_username(self, airline_username):
        """
        """
        pass

    def create(self, user_id, name, country_id):
        """
        """