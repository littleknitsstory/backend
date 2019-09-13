from django.db import models
from django.utils.translation import ugettext_lazy as _


class ModelMixin(models.Model):

    email = models.EmailField(_('Email'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    class Meta:
        abstract = True
