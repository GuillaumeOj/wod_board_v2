from django.contrib.auth.forms import BaseUserCreationForm

from users.models import User


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name")
