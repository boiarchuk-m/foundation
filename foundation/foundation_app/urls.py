from django.urls import path
from .views import LoginView, RegisterView,RequestListCreate, RequestDelete
from rest_framework.routers import DefaultRouter
from django.urls import path, include




urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path("requests/", RequestListCreate.as_view(), name="note-list"),
    path("requests/delete/<int:pk>/", RequestDelete.as_view(), name="delete-note"),
]