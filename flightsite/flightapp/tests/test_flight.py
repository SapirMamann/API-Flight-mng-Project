from rest_framework.test import APIClient
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
import pytest


# Use the @pytest.mark.django_db decorator to enable database access during tests.
@pytest.mark.django_db
class TestFlightsList:
    def setup_method(self):
        self.api_client = APIClient()


    def test_get_flights(self):
        url = reverse('flights-list')  
        response = self.api_client.get(url)

        assert response.status_code == 200  # Check if the GET request is successful

    # def create_test_user(self, username, password):
    #     return User.objects.create_user(username=username, password=password)


    # def test_create_airline(self):
    #     url = reverse('airlines')
    #     data = {'user': '59','name': 'Test Airline', 'country': '13'}
    #     response = self.api_client.post(url, data, format='json')

    #     self.assertEqual(response.status_code, 201)






# @pytest.mark.django_db
# def test_create_item(api_client):
#     # This test case simulates creating an Item through 
#     # a POST request to the API.
#     # It uses the reverse function to generate the URL for the 
#     # item-list view, which is likely associated with creating items.
#     url = reverse('item-list')  # Assuming you have a viewset named 'ItemViewSet'

#     # dictionary contains the data you want to send in the request body
#     data = {'name': 'Test Item', 'description': 'A test item'}

#     # api_client.post method sends a POST request to the URL with 
#     # the specified data.
#     response = api_client.post(url, data, format='json')

#     # assert statements check whether the response status code is 201 (HTTP Created), 
#     # indicating successful item creation.
#     assert response.status_code == 201
