from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscribe(models.Model):
    email = models.EmailField(_('Email'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    hidden = models.CharField(_('Hidden'), max_length=200)

    class Meta:
        verbose_name = _('Subscribe')
        verbose_name_plural = _('Subscribers')

    def __str__(self):
        return self.email
