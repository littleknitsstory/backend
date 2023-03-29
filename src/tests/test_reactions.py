import pytest


@pytest.fixture
def token(client, django_user_model):
    django_user_model.objects.create_user(
        username="test01@example.com", password="string8euwq"
    )
    res = client.post(
        "/api/v1/sign-up/",
        {"email": "test01@example.com", "password": "string8euwq"},
        format="json",
    )
    return f"Bearer {res.json().get('access')}"


@pytest.mark.django_db
def test_get_reaction(client):
    res = client.get("/api/v1/reactions/")
    assert res.status_code == 200
    assert res.json().get("count") == 0


@pytest.mark.django_db
def test_post_reaction(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    res = client.post(
        "/api/v1/reactions/?model_type=COMMENT&model_id=1",
        {"reaction": "RED_HEART"},
        format="json",
    )
    assert res.status_code == 201
    assert res.json().get("reaction") == "RED_HEART"
    assert res.json().get("model_type") == "COMMENT"
    assert res.json().get("model_id") == 1
    code = res.json().get("id")
    assert client.get(f"/api/v1/reactions/{code}/").status_code == 200


@pytest.mark.django_db
def test_put_reactions(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    res = client.post("/api/v1/reactions/", {"reaction": "RED_HEART"}, format="json")
    assert res.status_code == 201
    code = res.json().get("id")
    res = client.put(f"/api/v1/reactions/{code}/", {"reaction": "FIRE"}, format="json")
    assert res.status_code == 200
    assert res.json().get("reaction") == "FIRE"


@pytest.mark.django_db
def test_delete_reactions(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    res = client.post(
        "/api/v1/reactions/?model_type=COMMENT&model_id=1",
        {"reaction": "RED_HEART"},
        format="json",
    )
    assert res.status_code == 201
    code = res.json().get("id")
    assert client.delete(f"/api/v1/reactions/{code}/").status_code == 204
    assert client.get(f"/api/v1/reactions/{code}/").status_code == 404
