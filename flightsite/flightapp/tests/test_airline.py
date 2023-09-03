from rest_framework.test import APIClient
from django.urls import reverse
from django.test import TestCase
import pytest


@pytest.mark.django_db
class TestAirlinesList:
    def setup_method(self):
        self.api_client = APIClient()


    # def test_create_airline(self):
        
    #     # Set the token in the request's Authorization header
    #     # self.api_client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    #     url = reverse('airlines-list')
    #     data = {'user': '82', 'name': 'Test Airline', 'country': '13'}
    #     response = self.api_client.post(url, data, format='json')

    #     assert response.status_code == 200
