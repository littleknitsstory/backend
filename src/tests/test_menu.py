from venv.bin import pytest


@pytest.mark.django_db
@pytest.mark.urls("apps.menu.urls")
def test_menu_api(client):
	res = client.get('/api/v1/menu')
	assert res.status_code == 200
	
	
@pytest.mark.django_db
@pytest.mark.urls("apps.menu.urls")
def test_menu_api_id(client):
	res = client.get('/api/v1/menu/1')
	assert res.status_code == 200
	assert res.json() == {'id': 1, 'name': 'Home', 'url': '/'}


@pytest.mark.django_db
@pytest.mark.urls("apps.menu.urls")
def test_menu_api_id_not_found(client):
	res = client.get('/api/v1/menu/100')
	assert res.status_code == 404
	assert res.json() == {'detail': 'Not found.'}


@pytest.mark.django_db
@pytest.mark.urls("apps.menu.urls")
def test_menu_api_id_bad_request(client):
	res = client.get('/api/v1/menu/abc')
	assert res.status_code == 400
	assert res.json() == {'detail': 'Invalid ID.'}


@pytest.mark.django_db
@pytest.mark.urls("apps.menu.urls")
def test_menu_api_id_not_allowed(client):
	res = client.post('/api/v1/menu/1')
	assert res.status_code == 405
	assert res.json() == {'detail': 'Method "POST" not allowed.'}


@pytest.mark.django_db
@pytest.mark.urls("apps.menu.urls")
def test_menu_api_id_not_allowed_delete(client):
	res = client.delete('/api/v1/menu/1')
	assert res.status_code == 405
	assert res.json() == {'detail': 'Method "DELETE" not allowed.'}


@pytest.mark.django_db
@pytest.mark.urls("apps.menu.urls")
def test_menu_api_id_not_allowed_put(client):
	res = client.put('/api/v1/menu/1')
	assert res.status_code == 405
	assert res.json() == {'detail': 'Method "PUT" not allowed.'}

