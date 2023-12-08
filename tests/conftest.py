import uuid

import pytest
from rest_framework.test import APIClient


@pytest.fixture
def test_password():
    return str(uuid.uuid4())


@pytest.mark.django_db
@pytest.fixture
def create_user(django_user_model, test_password):
    def make_user(**kwargs):
        user_uuid = str(uuid.uuid4())
        kwargs["email"] = kwargs.get("email", f"{user_uuid}@foo.com")
        kwargs["username"] = kwargs.get("username", user_uuid)
        user = django_user_model.objects.create_user(**kwargs)
        user.set_password(test_password)
        user.save()

        return user

    return make_user


@pytest.fixture
def api_client():
    return APIClient()
