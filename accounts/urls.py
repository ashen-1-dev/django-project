# accounts/urls.py
from django.template.context_processors import request
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]