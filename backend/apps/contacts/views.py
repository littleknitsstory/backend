from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .models import Contact


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['name', 'email', 'feedback']
    template_name = 'contacts/contact_form.html'
