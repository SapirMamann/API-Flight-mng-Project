from django.urls import path, include
from .views import *


urlpatterns = [
    path('airline/<str:airline_id>/', AirlineCUD.as_view(), name='airline_crud'),
    path('airline/', AirlineCreate.as_view(), name='airline_create'),
]
