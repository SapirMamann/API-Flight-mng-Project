from django.contrib.auth.models import Permission
from rest_framework import generics
from django.utils.decorators import method_decorator

from ..serializers.permission import PermissionSerializer
from ..logics.permission import user_permissions


class PermissionList(generics.ListAPIView):
    """
    List of all permissions.
    The permission system is used by the Django admin site and are automatically created for each model (taken from 'Permission' description).
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    # @method_decorator(user_permissions('view_permission'))
    def get(self, request, *args, **kwargs):
        """
        works 12.04 15:19
        List of all permissions.
        """
        return self.list(request, *args, **kwargs)