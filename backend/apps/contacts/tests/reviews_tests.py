from django.test import TestCase
from apps.contacts.forms.reviews import ReviewForm


class TestReviews(TestCase):

    def test_valid_data(self):
        form = ReviewForm({
            'user_name': "Test name",
            'email': "test@test.com",
            'comment': "Hello world",
        })
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.user_name, "Test name")
        self.assertEqual(comment.email, "test@test.com")
        self.assertEqual(comment.comment, "Hello world")

    def test_blank_data(self):
        form = ReviewForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'user_name': ['Это поле обязательно.'],
            'email': ['Это поле обязательно.'],
            'comment': ['Это поле обязательно.'],
        })