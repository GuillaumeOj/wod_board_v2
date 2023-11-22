import pytest
from django.urls import reverse
from pytest_django.asserts import assertRedirects

from wods.models import Wod, WodCategoryChoices


@pytest.mark.django_db
def test_wod_create(client, create_user, test_password):
    url = reverse("wods:create")

    # Anonymous user is redirected to the login view
    response = client.get(url)
    expected_redirection_url = f"{reverse('users:login')}?next={url}"
    assertRedirects(response, expected_redirection_url)

    # Authenticated user can create a wod
    user = create_user()
    client.login(email=user.email, password=test_password)
    response = client.get(url)
    # The user see the form to create a WOD
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize(
    "name, category, error_keys",
    [
        ("", "", ["category"]),
        ("", "Foo", ["category"]),
        ("", WodCategoryChoices.EMOM, []),
    ],
)
def test_wod_create_cases(
    name, category, error_keys, client, create_user, test_password
):
    url = reverse("wods:create")
    user = create_user()
    client.login(email=user.email, password=test_password)

    data = {"name": name, "category": category}
    response = client.post(url, data=data)
    if response.status_code == 200 and error_keys:
        form = response.context.get("form")
        assert form.is_valid() is False

        for error_key in form.errors.keys():
            assert error_key in error_keys
    else:
        assert response.status_code == 302
        assert Wod.objects.get(category=category)
