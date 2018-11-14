# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from apps.contacts.forms.feedback import FeedbackForm
from apps.contacts.models import Feedback
from django.urls import reverse_lazy


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/contact_form.html'
    success_url = reverse_lazy('blog:blog-list')