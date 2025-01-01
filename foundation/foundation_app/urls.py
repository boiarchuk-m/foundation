from django.urls import path
from .views import LoginView, RegisterView, UserRequestView, ManagerRequestView
from rest_framework.routers import DefaultRouter
from django.urls import path, include




urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('requests/', UserRequestView.as_view()),  # Get, Post for Users
    path('requests/<int:pk>/', UserRequestView.as_view()),  # Update, Delete for Users
    path('manager/requests/', ManagerRequestView.as_view()),  # Get for Managers
    path('manager/requests/<int:pk>/', ManagerRequestView.as_view()), # Update for Managers
]