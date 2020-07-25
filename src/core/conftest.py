import pytest
from django.core.management import call_command


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("migrate")
        call_command("loaddata", "src/fixtures/account.json")
        call_command("loaddata", "src/fixtures/shop.json")


@pytest.fixture
def authorized_client(client, customer_user):
    client.login(username=customer_user.email, password="password")
    return client
