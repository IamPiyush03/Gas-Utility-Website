from django.urls import path
from .views import request_service, track_request, account_info, landing_page,signup

urlpatterns = [
    path('', landing_page, name='landing_page'), 
    path('request/', request_service, name='request_service'),
    path('track/', track_request, name='track_request'),
    path('account/', account_info, name='account_info'),
    path('signup/', signup, name='signup'),
]