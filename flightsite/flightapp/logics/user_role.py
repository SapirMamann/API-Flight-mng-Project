from ..dal.user_role import UserRoleDal


class UserRoleLogic():
    dal = UserRoleDal()

    def get_all(self):
        """
        Get all user roles
        """
        return self.dal.get_all() 


    def get_by_id(self, user_id):
        """
        Get user role by ID
        """
        return self.dal.get_by_id(user_id)


    def get_by_username(self, customer_username):
        """
        Get customer by username
        for login purposes,
        by entering username we'll get the customer
        """
        pass

    def create(self, user_id, first_name, last_name, address, phone, credit_card):
        """
        modify thisssssssssssss
        Create a new user role- based on information provided by user
        """
        return self.dal.create(user_id, first_name, last_name, address, phone, credit_card)
    
    
        
        

