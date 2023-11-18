from django.contrib.auth.forms import AuthenticationForm, BaseUserCreationForm
from django.forms import EmailField
from django.forms.widgets import EmailInput, TextInput
from django.utils.translation import gettext_lazy as _

from users.models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = (
            "email",
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
        )
        widgets = {
            "email": EmailInput(attrs={"autofocus": True, "placeholder": _("Email")}),
            "username": TextInput(attrs={"placeholder": _("Username")}),
            "first_name": TextInput(attrs={"placeholder": _("First Name")}),
            "last_name": TextInput(attrs={"placeholder": _("Last Name")}),
        }


class UserLoginForm(AuthenticationForm):
    username = EmailField(
        widget=EmailInput(attrs={"autofocus": True, "placeholder": _("Email")})
    )
