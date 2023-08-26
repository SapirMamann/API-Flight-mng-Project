from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.views import PasswordChangeView

from ..serializers.auth import ChangePasswordSerializer


class AuthLogic():

    def change_password(self, object, data):
        """
        Change password by providing the object and passwords
        """
        serializer = ChangePasswordSerializer(data=data)
        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not object.check_password(old_password):
                return Response({"old_password": "Wrong password."}, 
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            object.set_password(serializer.data.get("new_password"))
            object.save()
            print("okkkkkkkkkish")
            return Response({"detail": "Password changed successfully."},
                            status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
