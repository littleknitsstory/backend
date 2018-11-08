from django.test import TestCase, Client
from django.conf import settings
from apps.subscribe.models import Subscribe
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy


class TestSubscribe(TestCase):

    def setUp(self):
        self.client = Client()


    def test_app_in_settings(self):
        self.assertTrue('apps.subscribe' in settings.INSTALLED_APPS)

    def test_subscribe_view(self):
        url = reverse_lazy('subscribe:ajax_subscribe')
        response = self.client.post(url, {'email': 'test@test.com'})
        self.assertEqual(response.status_code, 200)

    # def test_delete_record(self):
    #     data = get_object_or_404(Subscribe, email='test@test.com')
    #     print(data)
    #     data.delete()


