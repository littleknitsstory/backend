import json

import pytest


@pytest.mark.django_db
@pytest.mark.urls("apps.contacts.urls")
def test_send_contacts_data(client):
    data = {
        "name": "hello",
        "message": "world",
        "phone_number": "88002000600",
        "email": "hello@world.com",
        "company": "hello_world inc.",
    }
    assert (
        client.post(
            "/contacts/", data=json.dumps(data), content_type="application/json"
        ).status_code
        == 201
    )


@pytest.mark.django_db
@pytest.mark.urls("apps.contacts.urls")
def test_send_contacts_bad_data_email(client):
    data = {
        "name": "hello",
        "message": "world",
        "phone_number": "88002000600",
        "email": "helloworld.com",
        "company": "hello_world inc.",
    }
    assert (
        client.post(
            "/contacts/", data=json.dumps(data), content_type="application/json"
        ).status_code
        == 400
    )
