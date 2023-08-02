from rest_framework import mixins, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from ..logics.user import UserLogic
from ..serializers.user import UserSerializer
from ..logics.permission import user_permissions
from ..models import User
from rest_framework.permissions import IsAuthenticated



class UsersList(generics.GenericAPIView,
                mixins.CreateModelMixin, 
                mixins.ListModelMixin):
    """
    Handles POST and GET requests.
    """
    logic = UserLogic()
    queryset = logic.get_all()
    serializer_class = UserSerializer
    
    @method_decorator(user_permissions('add_user'))
    def post(self, request, *args, **kwargs):
        """
        maybe i dont need this because im using auth register
        for admin use
        Create a new user.
        """
        return self.create(request, *args, **kwargs)
    

    # @method_decorator(user_permissions('can_view_all_users'))
    def get(self, request, *args, **kwargs):
        """
        List of all users.
        """
        # print(f"User permissions: {request.user.get_all_permissions()}")
        # print(f"User permissions: {request.user.has_perm('flightapp.view_user')}")

        # if request.user.has_perm('flightapp.view_user') is False:
        #     return Response('okkkkkk', status=403)

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
    
    @method_decorator(user_permissions('view_user'))
    def get(self, request, *args, **kwargs):
        """
        Getting a specific user.
        """
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
        obj = queryset.filter(username=self.kwargs.get(self.lookup_field)).first()
        if obj is not None:
            return obj
        # If user not found by either pk or username, raise a 404 error
        else:
            return Response({'error': 'User not found'}, status=404)

    @method_decorator(user_permissions('change_user'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific user.
        """
        return self.update(request, *args, **kwargs)
    

    @method_decorator(user_permissions('delete_user'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific user.
        """
        return self.destroy(request, *args, **kwargs)




class GetCurrentUserDetails(APIView):
    # permission_classes = (IsAuthenticated, )
    # im using this view because if i would have used the get user by id mixin view, i would have problem with the permissions
    
    def get(self, request, *args, **kwargs):
        # TODO: Try wit 'request.user' to get all of the user 
        # data instead of getting the object

        # Get user object
        print(request.user.id)
        try:
            print("try",request.user)
            user = User.objects.get(id=request.user.id)
            print("user", user)
            if user:
                print("if",request.user)
                return Response({
                    'username': user.username,
                    # 'isAdmin': user.is_admin,
                })
            # else:
            #     return Response({
            #         'error': 'User not found'
            #     }, status=404)
        except Exception as e:
            print("got except")
            return Response({
                'error': str(e)+'User not found'
            }, status=404)
        
        
# class GetUsername(APIView):
#     def get(self, request, *args, **kwargs):
#         print(request.user)
#         print("try",request.user)

#         return Response({
#             'username': request.user.username,
#             # 'isAdmin': user.is_admin,
#         })
#         try: 
#             user = User.objects.get(id=request.user.id)
#             print("user", user)
#             if user:
#                 print("if",request.user)
#         except Exception as e:
#             print("got except")
#             return Response({
#                 'error': str(e)+'User not found'
#             }, status=404)

    # print(request.user)
    # print(request.user.is_authenticated)
    # # Check if the user is authenticated
    # if request.user != 'AnonymousUser':
    #     print('in if', request.user)
    #     print('in if', request.headers)
    #     username = request.user.username
    #     # >>>>>>>>>>>>>>>>>>>>>>>>>>> change
    #     return JsonResponse({'username': 2})
    # else:
    #     # If the user is not authenticated, return an error or an empty response
    #     # return JsonResponse({'username': 'sa'})

    #     # ?>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>return 401
    #     print('in else')
    #     return JsonResponse({'error': 'User not authenticated'}, status=401)
        

# def get_username(request):
#     print(request.user)
#     print(request.user.is_authenticated)
#     # Check if the user is authenticated
#     if request.user != 'AnonymousUser':
#         print('in if', request.user)
#         print('in if', request.headers)
#         username = request.user.username
#         # >>>>>>>>>>>>>>>>>>>>>>>>>>> change
#         return JsonResponse({'username': 2})
#     else:
#         # If the user is not authenticated, return an error or an empty response
#         # return JsonResponse({'username': 'sa'})

#         # ?>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>return 401
#         print('in else')
#         return JsonResponse({'error': 'User not authenticated'}, status=401)