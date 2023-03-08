import pytest


@pytest.mark.django_db
@pytest.mark.urls("apps.account.urls")
def test_sign_up_short_pass(client):
    assert (
        client.post(
            "/sign-up/", {"email": "test@example.com", "password": "str"}, format="json"
        ).status_code
        == 400
    )


@pytest.mark.django_db
@pytest.mark.urls("apps.account.urls")
def test_sign_up_in_out(client):
    res = client.post(
        "/sign-up/",
        {"email": "test02@example.com", "password": "string8euwq"},
        format="json",
    )
    assert res.status_code == 201
    assert type(res.json().get("access")) == str

    res = client.post(
        "/sign-in/",
        {
            "username": "test02",
            "email": "test02@example.com",
            "password": "string8euwq",
        },
        format="json",
    )
    assert res.status_code == 200
    access_token = res.json().get("access")
    refresh_token = res.json().get("refresh")
    assert type(access_token) == str
    assert type(refresh_token) == str

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    res = client.post("/sign-out/", {"refresh": refresh_token}, format="json")
    assert res.status_code == 200


@pytest.mark.django_db
@pytest.mark.urls("apps.account.urls")
def test_get_profile(client, token):
    assert client.get("/profile/").status_code == 401
    client.credentials(HTTP_AUTHORIZATION=token)
    res = client.get("/profile/")
    assert res.status_code == 200
    username = res.json()[0].get("username")
    assert client.get(f"/profile/{username}/").status_code == 200


@pytest.mark.django_db
@pytest.mark.urls("apps.account.urls")
def test_put_profile(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    res = client.get("/profile/")
    assert res.status_code == 200
    username = res.json()[0].get("username")
    res = client.put(f"/profile/{username}/", {"address": "test"}, format="json")
    assert res.status_code == 200
    assert res.json().get("username") == username
    assert res.json().get("address") == "test"
