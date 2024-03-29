from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenBlacklistView)

from .views import *


urlpatterns = [
    # permissions
    path('permissions/', PermissionList.as_view(), name='permission-list'),

    # authentication
    path('auth/login/', CustomTokenObtainPairView.as_view(), name ='login'),     #name='token_obtain_pair'
    path('auth/refresh/', TokenRefreshView.as_view(), name ='auth_token_refresh'),      #name='token_refresh'
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='logout'),
    path('auth/password/change/', UpdatePassword.as_view(), name='password_change'),

    # admins
    path('admins/', AdminsList.as_view(), name='admins-list'),
    path('admins/<int:pk>/', AdminDetail.as_view(), name='admin-detail'),
    path('admins/get_admin_by_user_id/', GetAdminByUserID.as_view(), name='get-admin-by-user-id'),

    # users
    path('users/', UsersList.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

    path('users/get_current_user_details/', GetCurrentUserDetails.as_view(), name='get-current-user-details'),
    # path('users/get_username/', GetUsername.as_view(), name='get-current-user-details'),
    # path('users/get_username/', get_username, name='get-username'),

    # groupes
    path('groups/', GroupListCreate.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', GroupDetail.as_view(), name='group-detail'),
    path('groups/check/', GroupCheck.as_view(), name='group-check'),

    # countries
    path('countries/', CountriesList.as_view(), name='countries-list'),
    path('countries/<int:pk>/', CountryDetail.as_view(), name='country-detail'),

    # airlines
    path('airlines/', AirlinesList.as_view(), name='airlines-list'),
    path('airlines/<int:pk>/', AirlineDetail.as_view(), name='airline-detail'),
    path('airlines/get_airline_by_user_id/', GetAirlineByUserID.as_view(), name='get-airline-by-user-id'),
    
    # flights
    path('flights/', FlightsList.as_view(), name='flights-list'),
    path('flights/<int:pk>/', FlightDetail.as_view(), name='flight-detail'),
    path('get_flights/<str:country>/', FlightsByCountry.as_view(), name='flight-by-country'),
    path('searchflights/', SearchFlight.as_view(), name='search-flight'),
    path('airline_flights/', AirlineCompanyFlights.as_view(), name='airline-flights'),
    
    # tickets
    path('tickets/', TicketsList.as_view(), name='tickets-list'),
    path('tickets/<int:pk>/', TicketDetail.as_view(), name='ticket-detail'),
    path('my_tickets/<int:pk>/', TicketsByUserID.as_view(), name='ticket-by-user-id'),

    # customers
    path('customers/', CustomersList.as_view(), name='customers-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    path('customers/get_customer_by_user_id/', GetCustomerByUserID.as_view(), name='get-customer-by-user-id'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)     #used for showing views at the browser