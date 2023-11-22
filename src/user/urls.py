from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import RegistrationAPIView

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Verify JWT token
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/user/signup/", RegistrationAPIView.as_view(), name="register"),
]
