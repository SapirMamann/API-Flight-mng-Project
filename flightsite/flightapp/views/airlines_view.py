from rest_framework.views  import APIView, Response, status
from ..dal.airline import AirlineDal
from ..logics.airline import AirlineLogic
from ..models import AirlineCompany
from ..serializers.airline import AirlineCompanySerializer


class AirlineList(APIView):
    def post(self, request, format=None):
        """
        I can do this differently (like in my notebook) CHECK THIS.
        display the relevant form to admins in React - react will send an HTTP POST request to this endpoint
        Create a new airline company
        """
        airline_user_id = request.data['user']
        airline_name = request.data['name']
        airline_country_id = request.data['country']

        try:
            AirlineLogic.create(self, airline_user_id, airline_name, airline_country_id)
            
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)
    

    def get(self, request, format=None):
        """
        List of all Airline companies (displays only names)
        """
        try:
            airlines = AirlineDal.get_all(self)
            serializer = AirlineCompanySerializer(airlines, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:  #maybe another except 
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    

class AirlineDetail(APIView):
    # serializer_class = AirlineCompanySerializer()     #should i use this in here?
       
    def get(self, request, airline_id, format=None):
        """
        Getting a specific airline
        """
        try:
            logic = AirlineLogic()
            airline = logic.get_by_id(airline_id)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        serializer = AirlineCompanySerializer(airline)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, airline_id, format=None):
        """
        Updating a specific airline
        """
        logic = AirlineLogic()
        airline = logic.get_by_id(airline_id)

        serializer = AirlineCompanySerializer(airline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    


        # try:
        #     serializer = AirlineCompanySerializer(data=recieved_data)

        #     if serializer.is_valid():
        #         AirlineDal.update(airline_id, serializer.validated_data)

        #         # return Response(serializer.data, status=200)
        # except Exception as e:
        #     pass
    

    def delete(self, request, airline_id, format=None):
        """
        Delete a specific airline
        """
        try:
            airline = AirlineCompany.objects.get(id=airline_id)
            airline.delete()
        except:
            return Response("Airline not found", status=404)

        return Response(status=204)
    

        
