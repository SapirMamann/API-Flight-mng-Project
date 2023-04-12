from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator

from ..serializers.group import GroupSerializer
from ..logics.permission import user_permissions


class GroupListCreate(generics.GenericAPIView,
                      mixins.ListModelMixin, 
                      mixins.CreateModelMixin):
    """
    add logics = ...
    Handles POST and GET requests
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [IsAuthenticated]

    @method_decorator(user_permissions('add_group'))
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @method_decorator(user_permissions('view_group'))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    


class GroupDetail(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,                     
                    mixins.DestroyModelMixin):
    """
    Handles GET, PUT and Delete requests by passing a group id.
    """
    # logic = GroupLogic()
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @method_decorator(user_permissions('view_group'))
    def get(self, request, *args, **kwargs):
        """
        Getting a specific group.
        """
        return self.retrieve(request, *args, **kwargs)


    @method_decorator(user_permissions('change_group'))
    def put(self, request, *args, **kwargs):
        """
        Updating a specific group.
        """
        return self.update(request, *args, **kwargs)
    

    @method_decorator(user_permissions('delete_group'))
    def delete(self, request, *args, **kwargs):
        """
        Delete a specific group.
        """
        return self.destroy(request, *args, **kwargs)
