import pytest
from django.core.management import call_command

from src.apps.account.models import User


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("migrate")
        call_command("loaddata", "src/fixtures/account.json")
        call_command("loaddata", "src/fixtures/shop.json")


@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser("admin@example.com", "password")


@pytest.fixture
def authorized_client(client, customer_user):
    client.login(username=customer_user.email, password="password")
    return client
