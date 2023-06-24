from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterApiView,
    LogoutApiView,
    ChangePasswordApiView,
    CustomTokenObtainPairView,
)

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),
    path("login/refresh/", TokenRefreshView.as_view(), name="login_refresh"),
    path("register/", RegisterApiView.as_view(), name="register"),
    path(
        "change_password/<int:pk>/",
        ChangePasswordApiView.as_view(),
        name="change_password",
    ),
    path("logout/", LogoutApiView.as_view(), name="logout"),
]
