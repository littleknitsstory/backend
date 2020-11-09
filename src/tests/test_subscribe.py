import json

import pytest


@pytest.mark.django_db
@pytest.mark.urls("apps.subscribe.urls")
def test_subscribe(client):
    data = {
        "email": "hello@world.com",
    }
    assert (
        client.post(
            "/subscribe/", data=json.dumps(data), content_type="application/json"
        ).status_code
        == 201
    )
    assert (
        client.post(
            "/subscribe/", data=json.dumps(data), content_type="application/json"
        ).status_code
        == 400
    )


@pytest.mark.django_db
@pytest.mark.urls("apps.subscribe.urls")
def test_subscribe_bad_data_email(client):
    data = {
        "email": "helloworld.com",
    }
    assert (
        client.post(
            "/subscribe/", data=json.dumps(data), content_type="application/json"
        ).status_code
        == 400
    )
