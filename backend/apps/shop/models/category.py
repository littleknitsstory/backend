from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.mixins.mixin import SeoMixin


class Category(SeoMixin):
    title = models.CharField(_('Title'), max_length=120)
    slug = models.CharField(_('Slug'), max_length=120, unique=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title
