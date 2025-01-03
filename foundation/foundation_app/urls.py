from django.urls import path
from .views import LoginView, RegisterView,RequestListCreate, RequestDelete, UpdateRequestView, GetRequestView
from rest_framework.routers import DefaultRouter
from django.urls import path, include




urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path("requests/", RequestListCreate.as_view(), name="note-list"),
    path("requests/delete/<int:pk>/", RequestDelete.as_view(), name="delete-note"),
    path('requests/update/<int:pk>/', UpdateRequestView.as_view(), name='update_request'),
    path('get/<int:pk>/', GetRequestView.as_view(), name='get_request'),
]