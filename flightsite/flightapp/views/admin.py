from rest_framework.views  import APIView, Response, status
from ..dal.airline import AirlineDal
from ..logics.airline import AirlineLogic
from ..models import AirlineCompany, User
from ..serializers.customer import UserSerializer


class AdminList(APIView):
    """
    Handles POST and GET requests
    """

    # def post(self, request, format=None):
    #     """
    #     try calling data=request.data instead

    #     I can do this differently (like in my notebook) CHECK THIS.
    #     display the relevant form to admins in React - react will send an HTTP POST request to this endpoint
    #     Create a new airline company
    #     """
    #     airline_user_id = request.data['user']                          #getting all required fields from user in order to create a new instance
    #     airline_name = request.data['name']
    #     airline_country_id = request.data['country']

    #     try:
    #         self.logic.create(airline_user_id, airline_name, airline_country_id)
            
    #     except Exception as e:
    #         return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    #     return Response(status=status.HTTP_201_CREATED)                         #A new airline company created
    

    def get(self, request, format=None):
        """
        List of all Airline companies (displays only names)
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

# class AirlineDetail(APIView):
#     """
#     Handles GET, PUT and Delete requests by passing an airline id
#     """
#     #try putting try except here, and use mixin
#     #try  except Airline.DoesNotExist:
#     #
#     # serializer_class = AirlineCompanySerializer()     #should i use this in here?
#     logic = AirlineLogic()

#     def get(self, request, airline_id, format=None):
#         """
#         Getting a specific airline
#         """
#         try:
#             airline = self.logic.get_by_id(airline_id)
#         except Exception as e:
#             return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

#         serializer = AirlineCompanySerializer(airline)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#     def put(self, request, airline_id, format=None):
#         """
#         Updating a specific airline
#         """
#         try:
#             airline = self.logic.get_by_id(airline_id)
#         except Exception as e:
#             return Response(str(e), status=status.HTTP_404_NOT_FOUND)

#         serializer = AirlineCompanySerializer(airline, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    

#     def delete(self, request, airline_id, format=None):
#         """
#         Delete a specific airline
#         """
#         try:
#             airline = self.logic.get_by_id(airline_id)
#         # except Airline.DoesNotExist:
#         except Exception as e:
#             return Response(str(e), status=status.HTTP_404_NOT_FOUND)

#         airline.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)  #or 200
    

        
