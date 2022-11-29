import json

import pytest


@pytest.mark.django_db
@pytest.mark.urls("apps.account.urls")
def test_sign_up_short_pass(client):
    data = {"email": "userexample.com", "password": "string"}
    assert (
        client.post(
            "/sign-up/", data=json.dumps(data), content_type="application/json"
        ).status_code
        == 400
    )


@pytest.mark.django_db
@pytest.mark.urls("apps.account.urls")
def test_sign_up(client):
    data = {"email": "user_test0@example.com", "password": "string8euwq"}
    res = client.post(
        "/sign-up/", data=json.dumps(data), content_type="application/json"
    )
    assert type(res.json().get("access")) == str


@pytest.mark.django_db
@pytest.mark.urls("apps.account.urls")
def test_get_profile(client, headers):
    assert client.get("/profile/").status_code == 401
    assert client.get("/profile/", headers=headers).status_code == 201
