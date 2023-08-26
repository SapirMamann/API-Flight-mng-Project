from ..dal.user import *
from ..serializers.user import UserSerializer


class UserLogic():
    dal = UserDal()

    def get_all(self):
        """
        Get all users
        """
        return self.dal.get_all() 


    def get_by_id(self, id):
        """
        Get user by id
        """
        try:
            user = self.dal.get_by_id(id)
            serializer = UserSerializer(user)
            if user is not None:
                print(user)
                return serializer.data
        except Exception as e:
            print("exception in get current user details view", e)
            return None
        

    def retrieve_by_username(self):
        pass
