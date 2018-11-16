from django.test import TestCase, Client
from django.conf import settings
from apps.contacts.models import Subscribe
from django.urls import reverse_lazy


class TestSubscribe(TestCase):

    def setUp(self):
        self.client = Client()
        Subscribe.objects.create(email='fortest@test.com')

    def test_app_in_settings(self):
        self.assertTrue('apps.contacts' in settings.INSTALLED_APPS)

    def test_subscribe_with_right_email(self):
        url = reverse_lazy('subscribe:ajax_subscribe')
        response = self.client.post(
            url,
            {'csrfmiddlewaretoken': 'SCnkSPN1xCtYQzofKUKOwKocQLakxw4Bh87yBCvwsMpEzXlj184g5sZehV5ousYt', 'email': 'test@test.com'},
            format='json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['response'], 'success')

    def test_subscribe_with_wrong_email(self):
        url = reverse_lazy('subscribe:ajax_subscribe')
        response = self.client.post(
            url,
            {'csrfmiddlewaretoken': 'SCnkSPN1xCtYQzofKUKOwKocQLakxw4Bh87yBCvwsMpEzXlj184g5sZehV5ousYt', 'email': 'fortest@test.com'},
            format='json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['response'], 'Вы уже подписаны.')
