from rest_framework import mixins, generics
from django.utils.decorators import method_decorator

from ..logics.customer import CustomerLogic
from ..serializers.customer import CustomerSerializer
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

    # @method_decorator(user_permissions('add_customer'))
    def post(self, request, *args, **kwargs):
        """
        Create a customer. 
        Permission is allowed any.
        """
        return self.create(request, *args, **kwargs)


    @method_decorator(user_permissions('view_customer'))
    def get(self, request, *args, **kwargs):
        """
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

    @method_decorator(user_permissions('view_customer'))
    def get(self, request, *args, **kwargs):
        """
        Get a specific customer.
        """
        return self.retrieve(request, *args, **kwargs)


    @method_decorator(user_permissions('change_customer'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific customer.
        """
        return self.update(request, *args, **kwargs)
    

    @method_decorator(user_permissions('delete_customer'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific customer.
        """
        return self.destroy(request, *args, **kwargs)