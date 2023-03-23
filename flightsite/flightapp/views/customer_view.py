from rest_framework.views  import APIView, Response, status
from rest_framework import mixins, generics

from ..logics.customer import CustomerLogic
from ..models import Customer, User
from ..serializers.customer import CustomerSerializer


class CustomerList(generics.GenericAPIView,
                   mixins.CreateModelMixin, 
                   mixins.ListModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = CustomerLogic()
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        """
        Create a customer. 
        """
        return self.create(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        """
        List of all customers.
        """
        return self.list(request, *args, **kwargs)
    

class CustomerDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin):
    """
    Handles GET, PUT and Delete requests by passing an customer id.
    """
    logic = CustomerLogic()
     
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        """
        Get a specific customer
        """
        print(self.queryset) 
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        """
        Updating a specific customer
        """
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        """
        Delete a specific customer
        """
        return self.delete(request, *args, **kwargs)
