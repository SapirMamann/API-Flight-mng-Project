from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenBlacklistView)

from .views import *


urlpatterns = [
    #permissions
    path('permissions/', PermissionList.as_view(), name='permission-list'),

    #authentication
    path('auth/login/', TokenObtainPairView.as_view(), name ='auth_login'),     #name='token_obtain_pair'
    path('auth/refresh/', TokenRefreshView.as_view(), name ='auth_token_refresh'),      #name='token_refresh'
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='logout'),

    #admins
    path('admins/', AdminsList.as_view(), name='admins-list'),
    path('admins/<int:pk>/', AdminDetail.as_view(), name='admin-detail'),

    #users
    path('users/', UsersList.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    #groupes
    path('groups/', GroupListCreate.as_view(), name='group-list-create'),

    #countries
    path('countries/', CountriesList.as_view(), name='countries-list'),
    path('countries/<int:pk>/', CountryDetail.as_view(), name='country-detail'),

    #airlines
    path('airlines/', AirlinesList.as_view(), name='airlines-list'),
    path('airlines/<int:pk>/', AirlineDetail.as_view(), name='airline-detail'),
    
    #flights
    path('flights/', FlightsList.as_view(), name='flights-list'),
    path('flights/<int:pk>/', FlightDetail.as_view(), name='flight-detail'),
    
    #tickets
    path('tickets/', TicketsList.as_view(), name='tickets-list'),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name='ticket-detail'),

    #customers
    path('customers/', CustomersList.as_view(), name='customers-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)     #used for showing views at the browser