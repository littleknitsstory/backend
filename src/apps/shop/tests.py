import pytest
from django.core.management import call_command


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'src/fixtures/account.json')
        call_command('loaddata', 'src/fixtures/shop.json')


@pytest.mark.django_db
@pytest.mark.urls('apps.shop.urls')
def test_something(client):
    print(dir(client.get('/products/')))
    print(client)
    print(client.get('/products/').json())
    print(client.get('/products/').status_code)
