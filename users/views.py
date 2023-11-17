import typing

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from users.forms import UserCreationForm

if typing.TYPE_CHECKING:
    from users.models import User


class UserRegistrationView(CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserProfileView(LoginRequiredMixin, DetailView):
    model = settings.AUTH_USER_MODEL
    template_name = "users/user_profile.html"
    context_object_name = "user_profile"

    def get_object(self, queryset: QuerySet["User"] | None = None) -> "User":
        del queryset
        return self.request.user
