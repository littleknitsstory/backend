from django.views.generic import CreateView

from apps.contacts.forms.feedback import FeedbackForm
from apps.contacts.models import Feedback
from django.urls import reverse_lazy


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'contacts/contacts.html'
    success_url = reverse_lazy('blog:blog-list')

    def get_context_data(self, **kwargs):
        context = super(FeedbackCreateView, self).get_context_data(**kwargs)
        context['crumb_title'] = 'Контакты'
        context['crumb_url'] = reverse_lazy('feedback:contact_create')
        return context

