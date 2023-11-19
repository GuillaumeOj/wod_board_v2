from django.urls import path

from users.views import UserLoginView, UserLogoutView, UserProfileView, UserRegisterView

app_name = "users"
urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
