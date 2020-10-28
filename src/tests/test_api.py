import pytest


@pytest.mark.django_db
@pytest.mark.urls("apps.shop.urls")
def test_get_categories_url(client):
    assert client.get("/categories/").status_code == 200
    assert client.get("/categories/Toys/").status_code == 200


# @pytest.mark.django_db
# @pytest.mark.urls("apps.menu.urls")
# def test_get_menu_url(client):
# 	assert client.get("/menu/").status_code == 200
# 	assert client.get("/menu/1/").status_code == 200
#
#
# @pytest.mark.django_db
# @pytest.mark.urls("apps.blog.urls")
# def test_get_blog_url(client):
# 	assert client.get("/posts/").status_code == 200
# 	assert client.get("/posts/prosto-zapis-v-blog/").status_code == 200
