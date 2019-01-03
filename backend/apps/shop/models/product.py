from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
from djmoney.models.fields import MoneyField

from core.mixin import SeoMixin, ImagesMixin

from ckeditor.fields import RichTextField


class Product(SeoMixin, ImagesMixin):
    """ Product model """
    title = models.CharField(_('Title'), max_length=120)
    slug = models.CharField(_('Slug'), max_length=120, unique=True)
    description = RichTextField(_('Description'))
    price = MoneyField(_('Price'), null=True, blank=True, max_digits=14, decimal_places=2, default_currency='RU')
    sale = MoneyField(_('Sale'), null=True, blank=True, max_digits=14, decimal_places=2, default_currency='RU')
    is_active = models.BooleanField(_('Active'), default=True)
    category = models.ManyToManyField('Category',
                                      verbose_name=_('Category'),
                                      related_name='product_categories',
                                      blank=True)
    tags = models.ManyToManyField('tags.Tag', verbose_name=_('Tags'), related_name='product_tags', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='product_user',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse_lazy('shop:main')

    @property
    def get_custom_url(self):
        return reverse_lazy('shop:product_detail', kwargs={'slug': self.slug})

    @property
    def get_app_name(self):
        return 'Магазин'

    @property
    def get_price(self):
        return self.price

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
