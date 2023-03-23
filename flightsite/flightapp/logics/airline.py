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
        Get airline by username
        for login purposes,
        by entering username we'll get the airline
        """
        pass

    def create(self, user_id, name, country_id):
        """
        Create a new airline- based on information provided by user
        """
        return self.dal.create(user_id, name, country_id)
        
        
