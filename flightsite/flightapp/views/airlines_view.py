from rest_framework.views  import APIView, Response
from ..dal.airline import AirlineDal
from ..logics.airline import AirlineLogic
from ..models import AirlineCompany
from ..serializers.airline import AirlineCompanySerializer

class AirlineCUD(APIView):
    serializer_class = AirlineCompanySerializer
       
    def get(self, airline_id):
        """
        Getting a specific airline
        """
        try:
            airline = AirlineLogic.get_by_id(airline_id)
            data = self.serializer_class(airline).data
        except Exception as e:
            return Response(str(e), status=400)

        return Response(data, status=200)


    def delete(self, airline_id):
        """
        Delete a specific airline
        """
        try:
            airline = AirlineCompany.objects.get(id=airline_id)
            airline.delete()
        except:
            return Response("Airline not found", status=404)

        return Response(status=204)
    

    def put(self, request, airline_id):
        """
        Updating a specific airline
        """
        
        airline_user_id = request.data['user']
        airline_name = request.data['name']
        airline_country_id = request.data['country']

            
        recieved_data = {
            "name": airline_name,
            "user_id": airline_user_id,
            "country_id": airline_country_id
        }

        try:
            serializer = AirlineCompanySerializer(data=recieved_data)

            if serializer.is_valid():
                AirlineDal.update(airline_id, serializer.validated_data)

                # return Response(serializer.data, status=200)
        except Exception as e:
            pass


        return Response(serializer.errors, status=400)

        


class AirlineCreate(APIView):
    def get(self, request):
        """
        if i need to display all airlines exist, should this be in here????????????
        """
        try:
            airlines = AirlineDal.get_all(self)
            serializer = AirlineCompanySerializer(airlines, many=True)

            return Response(serializer.data, status=200)

        except Exception as e:
            return Response(str(e), status=400)

    

    def post(self, request):
        """
        Create a new airline
        display the relevant form to admins in React - react will send an HTTP POST request to this endpoint
        """
        # print(request.data['name'])

        airline_user_id = request.data['user']
        airline_name = request.data['name']
        airline_country_id = request.data['country']

        try:
            AirlineLogic.create(self, airline_user_id, airline_name, airline_country_id)
            
        except Exception as e:
            return Response(str(e), status=400)

        return Response(status=201)