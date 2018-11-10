from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from core.mixin import SeoMixin, ImagesMixin


class Product(SeoMixin, ImagesMixin, models.Model):
    """ Product model """
    title = models.CharField(_('Title'), max_length=120)
    slug = models.CharField(_('Slug'), max_length=120, unique=True)
    price = models.IntegerField(_('Price'), null=True, blank=True)
    active = models.BooleanField(_('Active'), default=True)
    category = models.ManyToManyField('Category', verbose_name=_('Category'), related_name='product_categories')
    tags = models.ManyToManyField('tags.Tag', verbose_name=_('Tags'), related_name='product_tags')

    def get_absolute_url(self):
        return reverse('shop:main')

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Product')

    def __str__(self):
        return self.title
