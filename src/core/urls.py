from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),  # Obtain and refresh JWT token
    path("", include("user.urls")),  # Obtain and refresh JWT token
]
