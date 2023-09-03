import pytest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# @pytest.fixture
# def user():
#     user_data_class = user_services.UserDataClass(
#         username="testuser",
#         email="someuser@example.com",
#         password="testpassword",
#         password2="testpassword",
#         groups="Customer"
#     )
#     user = user_services.create_user(user_dc=user_data_class)
#     return user

# import pytest

# @pytest.fixture
# def user():
#     # Create a user
#     user = User.objects.create_user(username='testuser', password='testpassword')
#     return user
