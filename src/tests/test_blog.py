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
def test_get_article_list(client):
    res = client.get("/api/v1/articles/")
    assert res.status_code == 200


@pytest.mark.django_db
def test_get_article(client):
    res = client.get("/api/v1/articles/prosto-zapis-v-blog/")
    assert res.status_code == 200


@pytest.mark.django_db
def test_get_article_time_for_read(client):
    res = client.get("/api/v1/articles/prosto-zapis-v-blog/")
    assert res.status_code == 200
    assert res.json().get("time_for_read") == 35


@pytest.mark.django_db
def test_post_article(client):
    res = client.post("/api/v1/articles/", {}, format="json")
    assert res.status_code == 405


@pytest.mark.django_db
def test_delete_article(client):
    res = client.delete("/api/v1/articles/prosto-zapis-v-blog/")
    assert res.status_code == 405


@pytest.mark.django_db
def test_add_bookmarks(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    res = client.post(
        "/api/v1/articles/prosto-zapis-v-blog/bookmarks/",
        {},
        format="json",
    )
    assert res.status_code == 201
    assert res.json().get("id") == 1
    assert res.json().get("article") == "prosto-zapis-v-blog"


@pytest.mark.django_db
def test_add_anonymous_bookmarks(client, token):
    res = client.post(
        "/api/v1/articles/prosto-zapis-v-blog/bookmarks/",
        {},
        format="json",
    )
    assert res.status_code == 401


@pytest.mark.django_db
def test_delete_not_bookmarks(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    res = client.delete(
        "/api/v1/articles/prosto-zapis-v-blog/bookmarks/",
        {},
        format="json",
    )
    assert res.status_code == 400


def test_delete_bookmarks(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    client.post(
        "/api/v1/articles/prosto-zapis-v-blog/bookmarks/",
        {},
        format="json",
    )
    res = client.delete(
        "/api/v1/articles/prosto-zapis-v-blog/bookmarks/",
        {},
        format="json",
    )
    assert res.status_code == 204


@pytest.mark.django_db
def test_get_article_not_is_bookmarked(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    res = client.get("/api/v1/articles/prosto-zapis-v-blog/")
    assert res.status_code == 200
    assert not res.json().get("is_bookmarked")


@pytest.mark.django_db
def test_get_article_is_bookmarked(client, token):
    client.credentials(HTTP_AUTHORIZATION=token)
    client.post(
        "/api/v1/articles/prosto-zapis-v-blog/bookmarks/",
        {},
        format="json",
    )
    res = client.get("/api/v1/articles/prosto-zapis-v-blog/")
    assert res.status_code == 200
    assert res.json().get("is_bookmarked")
