from rest_framework.test import APIClient
from django.urls import reverse
from django.test import TestCase
import pytest


@pytest.mark.django_db
class TestCountriesList:
    def setup_method(self):
        self.api_client = APIClient()


    def test_get_countries(self):
        # This view has allow any permission 
        url = reverse('countries-list')  #Using url name 
        response = self.api_client.get(url)

        assert response.status_code == 200  

