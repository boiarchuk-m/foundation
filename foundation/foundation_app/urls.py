from django.urls import path
from .views import LoginView, RegisterView, RequestViewSet, ManagerRequestViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'requests', RequestViewSet, basename='request')
router.register(r'manager_requests', ManagerRequestViewSet, basename='manager_request')


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]