import json

import pytest
from django.core.management import call_command
from djmoney.contrib.exchange.models import ExchangeBackend, Rate
from moneyed import Money, Currency

from src.apps.shop.models import Product


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("migrate")
        call_command("loaddata", "src/fixtures/account.json")
        call_command("loaddata", "src/fixtures/shop.json")


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_get_products_url(client):
    assert client.get("/products/").status_code == 200


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_post_orders_url(client):
    data = {
        "products": [{"product": 1, "amount": 1}],
        "phone": "string",
        "address": "string",
    }
    res = client.post(
        "/orders/", data=json.dumps(data), content_type="application/json"
    )
    assert res.status_code == 201
    assert res.json().get("status") == "NEW"
    assert isinstance(res.json().get("order_number"), str) is True

    code = res.json().get("order_number")
    assert client.get(f"/orders/{code}/").status_code == 200


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_post_orders_more_amounts_url(client):
    data = {
        "products": [{"product": 2, "amount": 200}],
        "phone": "string",
        "address": "string",
    }
    res = client.post(
        "/orders/", data=json.dumps(data), content_type="application/json"
    )
    assert res.status_code == 400


@pytest.mark.django_db
def test_product_get_money():
    backend = ExchangeBackend.objects.create(name="fixer.io", base_currency="RUB")
    rate = Rate.objects.create(currency="EUR", value=10, backend=backend)
    assert isinstance(rate, Rate) is True

    product = Product()
    product.price = Money(10, "RUB")
    price = product.get_money(value=product.price, currency="EUR")
    assert price.amount == 100.000000
    assert str(price.currency) == "EUR"
    assert isinstance(price.currency, Currency) is True
    assert isinstance(price, Money) is True

    price = product.get_money(value=product.price, currency="RUB")
    assert price.amount == 10
    assert str(price.currency) == "RUB"

    price = product.get_money(value=product.price, currency="USD")
    assert price == 0


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_get_product_and_lang_product_url(client, settings):
    res_1 = client.get("/products/test_slug/")
    assert res_1.status_code == 200
    assert res_1.json().get("title") == "test_title_ru"
    assert res_1.json().get("price") == "10.00 руб."

    # test_product_get_money save rate
    settings.LANGUAGE_CODE = "en"
    res_2 = client.get("/products/test_slug/")
    assert res_2.status_code == 200
    assert res_2.json().get("title") == "test_title_en"
    assert res_2.json().get("price") == "100.00 €"
