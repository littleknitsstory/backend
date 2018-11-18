from django.test import TestCase
from apps.contacts.forms.feedback import FeedbackForm
from captcha.models import CaptchaStore


class TestFeedback(TestCase):

    def setUp(self):
        self.captcha = CaptchaStore.objects.get(hashkey=CaptchaStore.generate_key())

    def test_valid_data(self):
        form = FeedbackForm({
            'name': "Test name",
            'email': "test@test.com",
            'feedback': "Hello world",
            'captcha_0': self.captcha.hashkey,
            'captcha_1': self.captcha.response
        })
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.name, "Test name")
        self.assertEqual(comment.email, "test@test.com")
        self.assertEqual(comment.feedback, "Hello world")

    def test_blank_data(self):
        form = FeedbackForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['Это поле обязательно.'],
            'email': ['Это поле обязательно.'],
            'feedback': ['Это поле обязательно.'],
            'captcha': ['Это поле обязательно.']
        })

