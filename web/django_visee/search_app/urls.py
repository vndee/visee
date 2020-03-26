# accounts/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', VerifyView.as_view(), name='verify_view'),
]