from django.urls import path

from users.views import UserProfileView, UserRegistrationView

urlpatterns = [
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("register/", UserRegistrationView.as_view(), name="register"),
]
