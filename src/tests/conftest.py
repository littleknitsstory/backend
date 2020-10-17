import json

import pytest
from django.core.management import call_command


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
	with django_db_blocker.unblock():
		call_command("migrate")
		call_command("loaddata", "src/fixtures/account.json")
		call_command("loaddata", "src/fixtures/shop.json")
		call_command("loaddata", "src/fixtures/exchange.json")


@pytest.fixture
def token(client, django_user_model):
	django_user_model.objects.create_user(
		username="user_test0001@example.com", password="string8euwq"
	)
	
	data = {"email": "user_test0001@example.com", "password": "string8euwq"}
	res = client.post(
		"/sign-up/", data=json.dumps(data), content_type="application/json"
	)
	return res.json().get("access")
