from django.contrib.auth.models import Permission
from rest_framework import generics
from rest_framework.permissions import BasePermission
from ..serializers.permission import PermissionSerializer



# class IsObjectOwner(BasePermission):
#         message = "You must be the owner of this object."
#         my_safe_methods = ['GET', 'PUT', 'PATCH', 'DELETE']

#     def has_permission(self, request, view):
#         if request.method in self.my_safe_methods:
#             return True
#         return False

#     def has_object_permission(self, request, view, obj):
#         if request.user.is_superuser:
#             return obj
#         else:
#             return obj == request.user
        

#For example, you might add the change_blogpost permission to the "Editors" group like this:        
#from django.contrib.auth.models import Permission

# change_blogpost_permission = Permission.objects.get(codename='change_blogpost')

# editors_group.permissions.add(change_blogpost_permission)



class PermissionList(generics.ListAPIView):
    """
    List of all permissions.
    The permission system is used by the Django admin site and are automatically created for each model (taken from 'Permission' description).
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer