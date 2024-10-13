from django.urls import path
from .views import submit_request, request_status

urlpatterns = [
    path('submit/', submit_request, name='submit_request'),
    path('status/', request_status, name='request_status'),
]