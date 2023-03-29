import pytest
from django.core.management import call_command
from rest_framework.test import APIClient


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("migrate")
        call_command("loaddata", "src/fixtures/blog.json")
        call_command("loaddata", "src/fixtures/menu.json")


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def token(client, django_user_model):
    django_user_model.objects.create_user(
        username="test01@example.com", password="string8euwq"
    )
    res = client.post(
        "/sign-up/",
        {"email": "test01@example.com", "password": "string8euwq"},
        format="json",
    )
    return f"Bearer {res.json().get('access')}"
