from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import RegisterView

urlpatterns = [
    path("authentication/register/", RegisterView.as_view(), name="register"),
    
    path(
        "authentication/token/",
        TokenObtainPairView.as_view(),
        name="authentication_obtain_token",
    ),
    path(
        "authentication/refresh/token/",
        TokenRefreshView.as_view(),
        name="authentication_refresh_token",
    ),
    path(
        "authentication/verify/token/",
        TokenVerifyView.as_view(),
        name="authentication_verify_token",
    ),
]
