from django.urls import path
from .views import manage_requests

urlpatterns = [
    path('manage/', manage_requests, name='manage_requests'),
]