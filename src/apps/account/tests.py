import pytest
from django.core.management import call_command

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


# @pytest.mark.django_db
# @pytest.mark.urls("apps.account.urls")
# def test_get_sign_up(client):
#     data = {"email": "user_test0@example.com", "password": "string8euwq"}
#     res = client.post(
#         "/sign-up/", data=json.dumps(data), content_type="application/json"
#     )
#
