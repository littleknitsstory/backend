from .mixin import ModelMixin
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Contact(ModelMixin):

    phone = models.CharField(max_length=12)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.user_name