from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *


urlpatterns = [
    path('airlines/', AirlineList.as_view(), name='airline-list'),
    path('airlines/<str:airline_id>/', AirlineDetail.as_view(), name='airline-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)