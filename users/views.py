import typing

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from users.forms import UserCreationForm, UserLoginForm

if typing.TYPE_CHECKING:
    from users.models import User


class UserRegisterView(CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = UserCreationForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")


class UserLoginView(LoginView):
    form_class = UserLoginForm
    redirect_authenticated_user = True
    template_name = "users/login.html"
    next_page = reverse_lazy("users:profile")


class UserLogoutView(LogoutView):
    template_name = "users/logout.html"
    next_page = reverse_lazy("home")


class UserProfileView(LoginRequiredMixin, DetailView):
    model = settings.AUTH_USER_MODEL
    template_name = "users/profile.html"
    context_object_name = "profile"

    def get_object(self, queryset: QuerySet["User"] | None = None) -> "User":
        del queryset
        return self.request.user
