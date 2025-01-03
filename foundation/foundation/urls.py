
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('foundation_app.urls')),
    path("app/token", TokenObtainPairView.as_view(), name='get_token'),
    path("app/token/refresh", TokenRefreshView.as_view(), name='refresh'),
]

