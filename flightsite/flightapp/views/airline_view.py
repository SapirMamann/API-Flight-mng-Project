from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..logics.airline import AirlineLogic
from ..serializers.airline import AirlineCompanySerializer
from ..logics.permission import user_permissions
from ..models import AirlineCompany, User, Country


class AirlinesList(generics.GenericAPIView,
                   mixins.CreateModelMixin, 
                   mixins.ListModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = AirlineLogic()
    queryset = logic.get_all()
    serializer_class = AirlineCompanySerializer    

    @method_decorator(user_permissions('flightapp.add_airlinecompany'))
    def post(self, request, *args, **kwargs):
        """
        Create a new airline company.
        """
        print("request.data",request.data)
        return self.create(request, *args, **kwargs)

    @method_decorator(user_permissions('flightapp.view_airlinecompany'))
    def get(self, request, *args, **kwargs):    
        """
        List of all Airline companies (displays only names).
        """
        return self.list(request, *args, **kwargs)
    


class AirlineDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                     
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing an airline id
    """
    logic = AirlineLogic()
    queryset = logic.get_all()
    serializer_class = AirlineCompanySerializer

    @method_decorator(user_permissions('flightapp.view_airlinecompany'))
    def get(self, request, *args, **kwargs):
        """
        Getting a specific airline
        """
        return self.retrieve(request, *args, **kwargs)


    @method_decorator(user_permissions('flightapp.change_airlinecompany'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific airline
        """
        return self.partial_update(request, *args, **kwargs)


    @method_decorator(user_permissions('flightapp.delete_airlinecompany'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific airline and associated user.
        """
      
        airline_instance = self.get_object()
        self.logic.delete_airline_with_user(airline_instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class GetAirlineByUserID(APIView):
    # permission_classes = (IsAuthenticated, )
    # im using this view because if i would have used the get user by id mixin view, i would have problem with the permissions
    
    def get(self, request, *args, **kwargs):
        print("here",request.user.id)
        request_user_id = request.user.id
        try:
            user = User.objects.get(id=request_user_id)
            print("user",user)
            airline_instance = AirlineCompany.objects.filter(user=user).first()
            print("admin_instance", airline_instance)
            serializer = AirlineCompanySerializer(airline_instance)
            
            if airline_instance:
                print("if",request.user)
                print(user)
                return Response(serializer.data)
            else:
                return Response({
                'error': str(e)+'airline not found, maybe signed in as an admin'
            }, status=404)

        except Exception as e:
            print("exception in GetAirlineByUserID view", e)
            return Response({
                'error': str(e)+'User not found'
            }, status=404)
