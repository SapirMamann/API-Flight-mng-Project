from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from django.http import JsonResponse

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



class GroupCheck(APIView):
    """
    """
    def get(self, request, *args, **kwargs):
        groups_from_request = str(request.GET.get('groups', ""))      #Get groups from the request, if its not provided in react, default to an empty str 

        user_group_list =[]     #Get the list of user's groups. 
        for group in request.user.groups.all():     #Turn queryset to list
            user_group_list.append(group.name)
        print(user_group_list)      #['Administrator']
        print(groups_from_request)      #groups=Administrator,+Airline+company
        for group in user_group_list:       #Loop through user's groups.
            print(group)        #Administrator
            if group in groups_from_request:        #If theres a match => send a "True" response to react side
                # print('yes')
                return JsonResponse({'result': True})
        else:
            print('no')
            return JsonResponse({'result': False})        
        
        # user_group = str(request.user.groups.all())     #get the user's group
        # print(groups_from_request)      #Administrator
      
        # user_group = list(request.user.groups.values_list('name', flat = True))     #get the user's group
        # print(f'user_group: {user_group}')  #user_group: <QuerySet [<Group: Administrator>]>

        # print(request.user)     #admin
        # print(f'request.user.groups: {request.user.groups}')     #admin
        # print(f'l =  {l}')      #l =  ['Administrator']

        # if l in groups_from_request:

        
        # groups_from_request = []
        # for obj in request.GET['groups[]']:
        #     for k,v in obj.items():
        #         groups_from_request.append(v)
