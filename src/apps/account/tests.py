import json

import pytest
from django.core import mail
from django.core.management import call_command


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("migrate")
        call_command("loaddata", "src/fixtures/account.json")
        call_command("loaddata", "src/fixtures/shop.json")


# @pytest.mark.django_db
# @pytest.mark.urls("apps.account.urls")
# def test_sign_up_short_pass(client):
#     data = {"email": "userexample.com", "password": "string"}
#     res = client.post(
#         "/sign-up/", data=json.dumps(data), content_type="application/json"
#     )
#     print(res.json())
#     # access
#     assert (
#         client.post(
#             "/sign-up/", data=json.dumps(data), content_type="application/json"
#         ).status_code
#         == 400
#     )


@pytest.mark.django_db
@pytest.mark.urls("apps.account.urls")
def test_ste():
    print("hello")


@pytest.mark.django_db
@pytest.mark.urls("apps.account.urls")
def test_get_sign_up(client):
    data = {"email": "user_test0@example.com", "password": "string8euwq"}
    print(data)
    res = client.post(
        "/sign-up/", data=json.dumps(data), content_type="application/json"
    )
    print(res.json())


#     assert (
#         client.post(
#             "/sign-up/", data=json.dumps(data), content_type="application/json"
#         ).status_code
#         == 201
#     )


# @pytest.mark.django_db
# @pytest.mark.urls("apps.account.urls")
# def test_1(client):
#     EMAIL_BACKEND = 'anymail.backends.test.EmailBackend'
#     data = {"email": "user_test1@example.com", "password": "string8euwq"}
#
#     res = client.post(
#         "/sign-up/", data=json.dumps(data), content_type="application/json"
#     )
#     assert len(mail.outbox) == 1
#     assert mail.outbox[0].to == ["user@example.com"]


#
# from django.core import mail
# from django.test import TestCase
# from django.test.utils import override_settings
#
# @override_settings(EMAIL_BACKEND='anymail.backends.test.EmailBackend')
# class SignupTestCase(TestCase):
#     # Assume our app has a signup view that accepts an email address...
#     def test_sends_confirmation_email(self):
#         self.client.post("/account/signup/", {"email": "user@example.com"})
#
#         # Test that one message was sent:
#         self.assertEqual(len(mail.outbox), 1)
#
#         # Verify attributes of the EmailMessage that was sent:
#         self.assertEqual(mail.outbox[0].to, ["user@example.com"])
#         self.assertEqual(mail.outbox[0].tags, ["confirmation"])  # an Anymail custom attr
#
#         # Or verify the Anymail params, including any merged settings defaults:
#         self.assertTrue(mail.outbox[0].anymail_send_params["track_clicks"])
