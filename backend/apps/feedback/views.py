from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from apps.contacts.forms.feedback import FeedbackForm
from apps.contacts.models.feedback import Feedback


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    fields = ['name', 'email', 'feedback', 'captcha']
    template_name = 'feedback/contact_form.html'
