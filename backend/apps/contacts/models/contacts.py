from .mixin import ModelMixin
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.urls import reverse_lazy


class Contact(ModelMixin):

    phone = models.CharField(max_length=12)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    @property
    def get_absolute_url(self):
        return reverse_lazy('shop:main')

    @property
    def get_app_name(self):
        return 'Контакты'
