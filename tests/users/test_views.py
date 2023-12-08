import pytest
from django.urls import reverse

from users.models import User


@pytest.mark.django_db
def test_registration(client):
    url = reverse("users:register")

    # Missing values for required fields
    data = {
        "email": "",
        "password": "",
        "username": "",
        "first_name": "",
        "last_name": "",
    }
    response = client.post(url, data=data)

    errors = response.data or {}
    expected_errors_keys = ["email", "password", "username"]
    assert response.status_code == 400
    assert len(errors.keys()) == len(expected_errors_keys)
    for error_key in errors.keys():
        assert error_key in expected_errors_keys

    # User is created
    data = {
        "email": "foo@bar.com",
        "password": "password",
        "username": "foo",
        "first_name": "",
        "last_name": "",
    }
    response = client.post(url, data=data)

    assert response.status_code == 201
    assert response.data["user"]["email"] == data["email"]
    assert response.data.get("token") is not None
    assert User.objects.count() == 1

    # User already exists and is not duplicated
    response = client.post(url, data=data)

    errors = response.data or {}
    expected_errors_keys = ["email", "username"]
    assert response.status_code == 400
    assert len(errors.keys()) == len(expected_errors_keys)
    for error_key in errors.keys():
        assert error_key in expected_errors_keys
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_login(client, create_user, test_password):
    url = reverse("users:login")

    data = {
        "email": "foo@bar.com",
        "password": test_password,
    }
    response = client.post(url, data=data)
    assert response.status_code == 400
    assert response.data.get("token") is None

    user = create_user()
    data = {
        "email": user.email,
        "password": test_password,
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    assert response.data.get("token") is not None


@pytest.mark.django_db
def test_user_profile(api_client, create_user):
    url = reverse("users:profile")

    # Anonymous user is redirect to the login view
    response = api_client.get(url)
    assert response.status_code == 401
    assert response.data["detail"].code == "not_authenticated"

    # Authenticated user can see their profile
    user = create_user()
    api_client.force_authenticate(user)
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data["email"] == user.email
