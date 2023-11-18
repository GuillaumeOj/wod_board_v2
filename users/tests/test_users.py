import pytest
from django.urls import reverse
from pytest_django.asserts import assertRedirects

from users.models import User


@pytest.mark.django_db
@pytest.mark.parametrize(
    "email, password1, password2, username, first_name, last_name, error_keys",
    [
        ("", "", "", "", "", "", ["email", "password1", "password2", "username"]),
        ("foo@bar.com", "", "", "", "", "", ["password1", "password2", "username"]),
        (
            "foo@bar.com",
            "password",
            "password",
            "foo",
            "",
            "",
            ["password1", "password2"],
        ),
        (
            "foo@bar.com",
            "strong_pass",
            "password",
            "foo",
            "",
            "",
            ["password2"],
        ),
        (
            "foo@bar.com",
            "strong_pass",
            "strong_pass",
            "foo",
            "",
            "",
            [],
        ),
        (
            "foo@bar.com",
            "strong_pass",
            "strong_pass",
            "foo",
            "",
            "",
            ["email"],
        ),
    ],
)
def test_registration(
    email, password1, password2, username, first_name, last_name, error_keys, client
):
    url = reverse("users:register")
    data = {
        "email": email,
        "password1": password1,
        "password2": password2,
        "username": username,
        "first_name": first_name,
        "last_name": last_name,
    }
    response = client.post(url, data=data)
    # If errors occured with the form, the template return 200 with a list of errors
    if response.status_code == 200 and error_keys:
        form = response.context.get("form")
        errors = form.errors or {}

        for error_key in errors.keys():
            assert error_key in error_keys
    # Else the user is redirected to the login form
    else:
        assert response.status_code == 302
        assert User.objects.get(email=email)


@pytest.mark.django_db
def test_user_profile(client, create_user, test_password):
    url = reverse("users:profile")

    # Anonymous user is redirect to the login view
    response = client.get(url)
    expected_redirection_url = (
        f"{reverse('users:login')}?next={reverse('users:profile')}"
    )
    assertRedirects(response, expected_redirection_url)

    # Authenticated user can see their profile
    user = create_user()
    client.login(email=user.email, password=test_password)
    response = client.get(url)
    assert response.status_code == 200
