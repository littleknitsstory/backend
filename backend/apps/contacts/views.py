from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    fields = ['name', 'email', 'feedback', 'captcha']
    template_name = 'contacts/contact_form.html'

