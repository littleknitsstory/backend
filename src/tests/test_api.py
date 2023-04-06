import pytest


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_get_categories_url(client):
    assert client.get("/categories/").status_code == 200
    assert client.get("/categories/Toys/").status_code == 200


@pytest.mark.django_db
@pytest.mark.urls("apps.menu.urls")
def test_get_menu_url(client):
    assert client.get("/menu/").status_code == 200
    assert client.get("/menu/1/").status_code == 200


@pytest.mark.django_db
@pytest.mark.urls("apps.blog.urls")
def test_get_blog_url(client):
    assert client.get("/articles/").status_code == 200
    assert client.get("/articles/prosto-zapis-v-blog/").status_code == 200


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_get_shop_url(client):
    assert client.get("/products/").status_code == 200
    assert client.get("/products/test_slug/").status_code == 200


@pytest.mark.django_db
@pytest.mark.urls("apps.reviews.urls")
def test_get_reviews_url(client):
    assert client.get("/reviews/").status_code == 200


@pytest.mark.django_db
@pytest.mark.urls("apps.slider.urls")
def test_get_slider_url(client):
    assert client.get("/sliders/").status_code == 200
