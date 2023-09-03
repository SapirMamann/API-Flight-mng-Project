from rest_framework.test import APIClient
from django.urls import reverse
from django.test import TestCase
import pytest


@pytest.mark.django_db
class TestAuthViews:
    def setup_method(self):
        self.api_client = APIClient()


    # def test_login(self):
    #     data = {'username': 'admin', 'password': 'jack2024'}
    #     url = reverse('login')
    #     response = self.api_client.post(url, data, format='json')
    #     print(response.data, "responseeee")

    #     assert response.status_code == 200


    # def test_register_view(self):
        # payload = dict(
        #     username="testuser",
        #     email="testuser@example.com",
        #     password="testpassword",
        #     password2="testpassword",
        #     groups="Customer"
        # )
        # data = {'username': 'testtest', 'email':'testuser@example.com', 'password': 'jack2024', 'password2': 'jack2024', 'groups': 'Customer'}
        # url = reverse('register')  #Using url name 
        # response = self.api_client.post(url, data, format='json')
        # print(response, "responseeee")
        # assert response.status_code == 201

