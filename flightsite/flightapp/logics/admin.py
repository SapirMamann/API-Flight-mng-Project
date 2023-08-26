from rest_framework.response import Response

from ..dal.admin import AdminDal 
from ..dal.user import UserDal
from ..serializers.admin import AdminSerializer


class AdminLogic():
    dal = AdminDal()

    def get_all(self):
        """
        Get all users
        """
        return self.dal.get_all()


    def get_admin_by_user_id(self, user_id):
        """
        Get admin instance by user id
        """
        user_dal = UserDal()
        
        try:
            user = user_dal.get_by_id(user_id)
            print("user",user)
            admin_instance = self.dal.get_by_user_field(user)
            # admin_instance = Administrator.objects.filter(user=user).first()
            print("admin_instance", admin_instance)
            if admin_instance:
                serializer = AdminSerializer(admin_instance)
                return Response(serializer.data)
        except Exception as e:
            print("exception in get_admin_by_user_id logic", e)
            return Response({
                'error': str(e) + 'User not found'
            }, status=404)
        

    def delete_admin_with_user(self, admin_instance):
        """
        Delete admin instance and associated user instance
        """
        user_instance = admin_instance.user

        # Delete the admin instance
        admin_instance.delete()

        # Delete the user instance
        user_instance.delete()

