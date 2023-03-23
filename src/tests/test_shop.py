import json

import pytest

pytestmark = pytest.mark.django_db

пше


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_get_products_url(client):
    products = client.get("/products/").json()
    assert type(products["results"][0]["id"]) == int


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_post_orders_url(client):
    data = {
        "products": [{"product": 1, "amount": 1}],
        "phone": "string",
        "address": "string",
    }
    res = client.post(
        "/orders/",
        data=json.dumps(data),
        content_type="application/json",
    )
    assert res.status_code == 201
    assert res.json().get("status") == "NEW"
    assert isinstance(res.json().get("order_number"), str)
    code = res.json().get("order_number")
    assert client.get(f"/orders/{code}/").status_code == 200


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_post_orders_double_product_url(client):
    data = {
        "products": [{"product": 1, "amount": 1}, {"product": 1, "amount": 1}],
        "phone": "string",
        "address": "string",
    }
    res = client.post(
        "/orders/", data=json.dumps(data), content_type="application/json"
    )
    assert res.status_code == 400
    assert res.json().get("products") == ["The order contains a duplicate of the goods"]


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
    assert res.json().get("products") == ["Product less than requested"]


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_get_product_and_lang_product_url(client, settings):
    res_1 = client.get("/products/test_slug/")
    assert res_1.status_code == 200
    assert res_1.json().get("title") == "test_title_ru"
    assert res_1.json().get("price") == "10.00"  # "10.00 ₽"
    # test_product_get_money save rate
    settings.LANGUAGE_CODE = "en"
    res_2 = client.get("/products/test_slug/")
    assert res_2.status_code == 200
    assert res_2.json().get("title") == "test_title_en"
