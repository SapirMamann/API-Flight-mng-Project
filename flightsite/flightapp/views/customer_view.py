from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from ..models import Customer
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


    @method_decorator(user_permissions('flightapp.view_customer'))
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

    # @method_decorator(user_permissions('flightapp.view_customer'))
    def get(self, request, *args, **kwargs):
        """
        Get a specific customer.
        needs to add permission of only request.user
        """
        print("user", request.user.get_group_permissions())
        return self.retrieve(request, *args, **kwargs)
    

    def get_object(self):
        """
        wondering if it could be a problem to provide this view to users. (maybe user has the same id? could this happen?)
        Override get_object() to allow for retrieving the customer by user id. better as username
        """
        # replace to logic>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        queryset = self.get_queryset()
        # Try to get the user by pk
        obj = queryset.filter(pk=self.kwargs.get(self.lookup_field)).first()
        if obj is not None:
            return obj
        # # If user not found by pk, try to get it by user id
        # obj = queryset.filter(user=self.kwargs.get(self.lookup_field)).first()
        # if obj is not None:
        #     return obj
        # If customer not found by either pk or userid, raise a 404 error
        else:
            return Response({'error': 'User not found'}, status=404)


    @method_decorator(user_permissions('flightapp.change_customer'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific customer.
        """
        return self.update(request, *args, **kwargs)
    

    @method_decorator(user_permissions('flightapp.delete_customer'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific customer and associated user.
        """
        customer_instance = self.get_object()
        self.logic.delete_customer_with_user(customer_instance)
        return Response(status=status.HTTP_204_NO_CONTENT)



class GetCustomerByUserID(APIView):
    # permission_classes = (IsAuthenticated, )
    # im using this view because if i would have used the get user by id mixin view, i would have problem with the permissions
    logic = CustomerLogic()

    def get(self, request, *args, **kwargs):
        request_user_id = request.user.id
        return self.logic.get_by_user_id(request_user_id)


        # print("here",request.user.id)
        # request_user_id = request.user.id
        # try:
        #     user = User.objects.get(id=request_user_id)
        #     print("user",user)
        #     customer = Customer.objects.filter(user=user).first()
        #     print("customer", customer)
        #     serializer = CustomerSerializer(customer)
            
        #     if user:
        #         print("if",request.user)
        #         print(user)
        #         return Response(serializer.data)
        # except Exception as e:
        #     print("exception in get customer by user id view", e)
        #     return Response({
        #         'error': str(e)+'User not found'
        #     }, status=404)
