from rest_framework.permissions import BasePermission


class GroupPermission(BasePermission):
    """
    Check whether a user has permission to access a view. 
    """
    def has_permission(self, request, view):
        required_groups = getattr(view, 'required_groups', {})      #dictionary that maps view methods to the groups that are required to access them
        user_groups = request.user.groups.all()     #retrieve (to a queryset) all the groups that the current user belongs to 
        return any(group in user_groups for group in required_groups)       #check whether any (at least one) of the required groups for the view are in the user's group queryset 
