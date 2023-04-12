from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status


class CanViewCountries(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('flightapp.can_view_countries')

# def get_user_groups_from_token(token):
#     """
#     Given a JWT token, return the list of groups associated with the user.
#     """
#     decoded_token = JWTAuthentication(token)
#     user_groups = decoded_token.get('groups', [])
#     return user_groups

    

def user_permissions(permission):
    """
    Decorator that checks if a user has a permission to visit a certain page.
    User doesnt have the required permission -> return status 403
    """
    def decorator(view_function):
        def wrapper(request, *args, **kwargs):
            # Check if a user has a group and the required permission
            if request.user.user_role and request.user.user_role.permissions.filter(codename=permission).exists():

                # print(request.user) #admin
                # print(request.user.user_role) #Administrator
                # print(request.user.user_role.permissions.filter(codename='can_view_countries').exists()) #auth.Permission.None

                return view_function(request, *args, **kwargs)
            
            else:       #User does not have the required permission -> return status 403, with message
                return Response({'error': "You don't have the permission to visit this page"}, status=status.HTTP_403_FORBIDDEN)
        return wrapper
    return decorator