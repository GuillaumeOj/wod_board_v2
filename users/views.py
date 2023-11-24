import typing

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from core.types import HtmxHttpRequest
from users.forms import UserCreationForm, UserLoginForm

if typing.TYPE_CHECKING:
    from users.models import User


class UserRegisterView(CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = UserCreationForm
    template_name: str = "users/register_base.html"
    success_url = reverse_lazy("users:login")
    request: HtmxHttpRequest

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return ["users/register_partial.html"]
        return [self.template_name]


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name: str = "users/login_base.html"
    next_page = reverse_lazy("users:profile")
    request: HtmxHttpRequest

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return ["users/login_partial.html"]
        return [self.template_name]


class UserLogoutView(LogoutView):
    template_name = "users/logout.html"
    next_page = reverse_lazy("home")


class UserProfileView(LoginRequiredMixin, DetailView):
    model = settings.AUTH_USER_MODEL
    template_name: str = "users/profile_base.html"
    context_object_name = "profile"
    request: HtmxHttpRequest

    def get_template_names(self) -> list[str]:
        if self.request.htmx:
            return ["users/profile_partial.html"]
        return [self.template_name]

    def get_object(self, queryset: QuerySet["User"] | None = None) -> "User":
        return self.request.user
