# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('order-history/', views.order_history, name='order_history'),
]