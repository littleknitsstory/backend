from django.utils.translation import ugettext_lazy as _
from .mixin import ModelMixin
from django.db import models


class Subscribe(ModelMixin):
    email = models.EmailField(_('Email'))
    hidden = models.CharField(_('Hidden'), max_length=200)

    class Meta:
        verbose_name = _('Subscribe')
        verbose_name_plural = _('Subscribers')

    def __str__(self):
        return self.email