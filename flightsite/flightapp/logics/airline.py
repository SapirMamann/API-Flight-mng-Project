from rest_framework.response import Response

from ..dal.airline import AirlineDal
from ..dal.user import UserDal
from ..serializers.airline import AirlineCompanySerializer


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


    def get_by_user_id(self, user_id):
        """
        Get airline by user ID
        """
        user_dal = UserDal()

        try: 
            user = user_dal.get_by_id(user_id)
            # print("user",user)
            airline_instance = self.dal.get_by_user_field(user)
            # print("airline_instance", airline_instance)
            if airline_instance:
                serializer = AirlineCompanySerializer(airline_instance)
                return Response(serializer.data)
            else:
                return Response({
                    'error': str(e)+'airline not found, maybe signed in as an admin'
                }, status=404)
        except Exception as e:
            print("exception in get_airline_by_user_id logic", e)
            return Response({
                'error': str(e) + 'User not found'
            }, status=404)
   

    def delete_airline_with_user(self, airline_instance):
        user_instance = airline_instance.user

        # Delete the airline instance
        airline_instance.delete()

        # Delete the user instance
        user_instance.delete()