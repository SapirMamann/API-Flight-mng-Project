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

    def delete_airline_with_user(self, airline_instance):
        user_instance = airline_instance.user

        # Delete the airline instance
        airline_instance.delete()

        # Delete the user instance
        user_instance.delete()