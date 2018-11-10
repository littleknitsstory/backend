from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    feedback = models.TextField(_('Feedback'))
    name = models.CharField(_('Name'), max_length=120)
    email = models.EmailField(_('Email'))

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.feedback[:25]
