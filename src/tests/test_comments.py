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
def test_get_comments(client):
    res = client.get("/api/v1/comments/")
    assert res.status_code == 200
    assert res.json().count == 0


@pytest.mark.django_db
def test_post_comments(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    res = client.post(
        "/api/v1/comments/?model_type=COMMENT&model_id=1",
        {"text": "test"},
        format="json",
    )
    assert res.status_code == 201
    assert res.json().get("text") == "test"
    assert res.json().get("model_type") == "COMMENT"
    assert res.json().get("model_id") == 1
    code = res.json().get("id")
    assert client.get(f"/api/v1/comments/{code}/").status_code == 200


@pytest.mark.django_db
def test_put_comments(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    res = client.post("/api/v1/comments/", {"text": "test"}, format="json")
    assert res.status_code == 201
    code = res.json().get("id")
    res = client.put(f"/api/v1/comments/{code}/", {"text": "test text"}, format="json")
    assert res.status_code == 200
    assert res.json().get("text") == "test text"


@pytest.mark.django_db
def test_delete_comments(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    res = client.post(
        "/api/v1/comments/?model_type=COMMENT&model_id=1",
        {"text": "test"},
        format="json",
    )
    assert res.status_code == 201
    code = res.json().get("id")
    assert client.delete(f"/api/v1/comments/{code}/").status_code == 204
    assert client.get(f"/api/v1/comments/{code}/").status_code == 404
