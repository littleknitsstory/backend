import json

import pytest
from django.core.management import call_command


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("migrate")
        call_command("loaddata", "src/fixtures/account.json")
        call_command("loaddata", "src/fixtures/shop.json")


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_post_orders_url(client):
    data = {
        "products": [{"product": 2, "amount": 1}],
        "phone": "string",
        "address": "string",
    }
    res = client.post("/orders/", data=json.dumps(data),  content_type='application/json')
    assert res.status_code == 201
    assert res.json().get("status") == "NEW"
    assert type(res.json().get("order_number")) == str


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_get_products_url(client):
    assert client.get("/products/").status_code == 200
