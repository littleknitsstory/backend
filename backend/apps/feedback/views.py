from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .forms import FeedbackForm
from .models import Feedback


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    fields = ['name', 'email', 'feedback', 'captcha']
    template_name = 'feedback/contact_form.html'
