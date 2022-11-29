import json

import pytest


@pytest.fixture
def headers(client, django_user_model):
    django_user_model.objects.create_user(
        username="user_test0001@example.com",
        password="string8euwq",
    )
    data = {"email": "user_test0001@example.com", "password": "string8euwq"}
    res = client.post(
        "/api/v1/sign-up/",
        data=json.dumps(data),
        content_type="application/json",
    )
    return {"Authorization": f"Bearer {res.json().get('access')}"}


@pytest.mark.django_db
@pytest.mark.urls("apps.comments.urls")
def test_get_comments(client):
    res = client.get("/comments/")
    assert res.status_code == 200
    assert res.json().get("count") == 0

@pytest.mark.django_db
#@pytest.mark.urls("apps.comments.urls")
def test_post_comments(client, headers):
    data = {"text": "test text"}
    res = client.post(
        "/api/v1/comments/?model_type=COMMENT&model_id=1",
        headers=headers,
        data=json.dumps(data),
        content_type="application/json",
    )
    assert res.status_code == 201
    assert res.json().get("text") == "test text"
    assert res.json().get("model_type") == "COMMENT"
    assert res.json().get("model_id") == 1
    code = res.json().get("id")
    assert client.get(f"/comments/{code}/").status_code == 200

@pytest.mark.django_db
#@pytest.mark.urls("apps.comments.urls")
def test_put_comments(client, headers):
    data = {"text": "text"}
    res = client.post(
        "/api/v1/comments/",
        headers=headers,
        data=json.dumps(data),
        content_type="application/json",
    )
    assert res.status_code == 201
    code = res.json().get("id")
    data = {"text": "test text"}
    res = client.put(
        f"/api/v1/comments/{code}/",
        headers=headers,
        data=json.dumps(data),
        content_type="application/json",
    )
    assert res.status_code == 200
    assert res.json().get("text") == "test text"

@pytest.mark.django_db
#@pytest.mark.urls("apps.comments.urls")
def test_delete_comments(client, headers):
    data = {"text": "test text"}
    res = client.post(
        "/api/v1/comments/?model_type=COMMENT&model_id=1",
        headers=headers,
        data=json.dumps(data),
        content_type="application/json",
    )
    assert res.status_code == 201
    code = res.json().get("id")
    res = client.delete(f"/api/v1/comments/{code}/", headers=headers)
    assert res.status_code == 204
    res = client.get(f"/api/v1/comments/{code}/")
    assert res.status_code == 404
