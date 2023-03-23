from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from .views.customer_view import CustomerList, CustomerDetail
from .views.admin import AdminList

urlpatterns = [
    path('admins/', AdminList.as_view(), name='admin-list'),

    #airlines
    path('airlines/', AirlineList.as_view(), name='airline-list'),
    path('airlines/<str:airline_id>/', AirlineDetail.as_view(), name='airline-detail'),

    #customers
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),

    path('auth/login/', TokenObtainPairView.as_view(), name ='auth_login'),     #name='token_obtain_pair'
    path('auth/refresh/', TokenRefreshView.as_view(), name ='auth_token_refresh'),      #name='token_refresh'
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),

    # flights
    # ...
]

urlpatterns = format_suffix_patterns(urlpatterns)