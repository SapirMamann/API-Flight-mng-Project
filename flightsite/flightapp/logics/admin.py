from ..dal.admin import AdminDal 


class AdminLogic():
    dal = AdminDal()

    def get_all(self):
        """
        Get all users
        """
        return self.dal.get_all()

    def delete_admin_with_user(self, admin_instance):
        user_instance = admin_instance.user

        # Delete the admin instance
        admin_instance.delete()

        # Delete the user instance
        user_instance.delete()