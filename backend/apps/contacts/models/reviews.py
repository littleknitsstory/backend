from .mixin import ModelMixin
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Review(ModelMixin):

    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return self.user_name