import uuid

import pytest


@pytest.fixture
def test_password():
    return str(uuid.uuid4())


@pytest.fixture
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        user_uuid = str(uuid.uuid4())
        kwargs["password"] = test_password
        kwargs["email"] = kwargs.get("email", f"{user_uuid}@foo.com")
        kwargs["username"] = kwargs.get("username", user_uuid)
        return django_user_model.objects.create_user(**kwargs)

    return make_user
