from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.mixin.mixin import ImagesMixin


class Slider(ImagesMixin):
    """ Slider model """

    title = models.CharField(_('Title'), max_length=120)
    slug = models.CharField(_('Slug'), max_length=120, unique=True)
    sub_title = models.CharField(_('Sub Title'), max_length=120, blank=True)
    active = models.BooleanField(_('Active'), default=True)
    ordering = models.IntegerField(_('Ordering'))
    link = models.URLField(_('Link'), blank=True)

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')

    def __str__(self):
        return self.title
