import pytest


@pytest.mark.urls('apps.shop.urls')
def test_something(client):
    print('HeLLO WORLD')
    print(client.get('/orders/').content)
    # assert 'Success!' in client.get('/order/').content