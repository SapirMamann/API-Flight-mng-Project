from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group

from ..serializers.group import GroupSerializer


class GroupListCreate(mixins.ListModelMixin, 
                      mixins.CreateModelMixin, 
                      generics.GenericAPIView):
    """
    add logics = ...
    Handles POST and GET requests
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
