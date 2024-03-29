from rest_framework import mixins, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password

from ..logics.user import UserLogic
from ..serializers.user import UserSerializer
from ..logics.permission import user_permissions
from ..models import User


class UsersList(generics.GenericAPIView,
                mixins.CreateModelMixin, 
                mixins.ListModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = UserLogic()
    queryset = logic.get_all()
    serializer_class = UserSerializer
    
    @method_decorator(user_permissions('auth.add_user'))
    def post(self, request, *args, **kwargs):
        """
        maybe i dont need this because im using auth register
        for admin use
        Create a new user.
        """
        return self.create(request, *args, **kwargs)
    

    @method_decorator(user_permissions('can_view_all_users'))
    def get(self, request, *args, **kwargs):
        """
        List of all users.
        """
        return self.list(request, *args, **kwargs)



class UserDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                     
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing a user id.
    """    
    logic = UserLogic()
    queryset = logic.get_all()
    serializer_class = UserSerializer
    
    @method_decorator(user_permissions('auth.view_user'))
    def get(self, request, *args, **kwargs):
        """
        Getting a specific user.
        """        
        print("user", request.user.get_group_permissions())
        return self.retrieve(request, *args, **kwargs)

    
    def get_object(self):
        """
        Override get_object() to allow for retrieving the user by either
        pk or username.
        """

        # replace to logic>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        queryset = self.get_queryset()
        # Try to get the user by pk
        obj = queryset.filter(pk=self.kwargs.get(self.lookup_field)).first()
        if obj is not None:
            return obj
        # If user not found by pk, try to get it by username
        # i dont think it works because i set the url as int
        obj = queryset.filter(username=self.kwargs.get(self.lookup_field)).first()
        if obj is not None:
            return obj
        # If user not found by either pk or username, raise a 404 error
        else:
            return Response({'error': 'User not found'}, status=404)


    @method_decorator(user_permissions('auth.change_user'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific user.
        """
        return self.update(request, *args, **kwargs)

        # user = request.user.username
        # print("user", user)
        # password = request.data.get('password')
        # print(password, "password")
        # authenticated_user = authenticate(username=user, password=password)
        # print("authenticated_user", authenticated_user)
        # if authenticated_user is not None:
        #     print("authenticated_user", authenticated_user)
        #     authenticated_user.set_password(password)
        #     authenticated_user.save()
        #     return Response({'message': 'Profile updated successfully'}, status=200)

        # else:
        #     return Response({'error': 'Wrong password'}, status=401)
    

    @method_decorator(user_permissions('auth.delete_user'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific user.
        """
        return self.destroy(request, *args, **kwargs)



class GetCurrentUserDetails(APIView):
    logic = UserLogic()
    # permission_classes = (IsAuthenticated, )
    # im using this view because if i would have used the get user by id mixin view, i would have problem with the permissions
    # Used for setting the stored state
    def get(self, request, *args, **kwargs):
        request_user_id = request.user.id
        response = self.logic.get_by_id(request_user_id)
        if response is not None:
            # print(response, "response of get current user details view")
            return Response(response, status=200)
        else:
            return Response({'error': 'User not found'}, status=404)
        

        
class GetUsername(APIView):
    def get(self, request, *args, **kwargs):
        # print(request.user)
        # print("try",request.user)
        if request.user.is_authenticated:
            print("authenticated",request.user)
        else:
            print("not authenticated",request.user)
        return Response({
            'username': request.user.username,
            # 'isAdmin': user.is_admin,
        })
       