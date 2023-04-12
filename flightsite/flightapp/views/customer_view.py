from rest_framework import mixins, generics

from ..logics.customer import CustomerLogic
from ..serializers.customer import CustomerSerializer


from django.utils.decorators import method_decorator
from ..logics.permission import user_permissions

class CustomersList(generics.GenericAPIView,
                   mixins.CreateModelMixin, 
                   mixins.ListModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = CustomerLogic()
    queryset = logic.get_all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        """
        works 24.03 16:25
        Create a customer. 
        """
        return self.create(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        """
        works 24.03 16:20
        List of all customers.
        """
        return self.list(request, *args, **kwargs)
    


class CustomerDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing a customer id.
    """
    logic = CustomerLogic()
    queryset = logic.get_all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        """
        works 24.03 16:21
        Get a specific customer.
        """
        return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        """
        works 24.03 16:23
        Updating a specific customer.
        """
        return self.update(request, *args, **kwargs)
    

    def delete(self, request, *args, **kwargs):
        """
        works 24.03 16:24
        Delete a specific customer.
        """
        return self.destroy(request, *args, **kwargs)