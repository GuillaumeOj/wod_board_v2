from django.urls import path
from knox.views import LogoutAllView, LogoutView

from users.views import UserLoginView, UserProfileView, UserRegisterView

app_name = "users"
urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("logoutall/", LogoutAllView.as_view(), name="logoutall"),
]
