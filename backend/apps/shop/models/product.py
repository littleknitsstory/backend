from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
from core.mixin import SeoMixin, ImagesMixin

from ckeditor.fields import RichTextField


class Product(SeoMixin, ImagesMixin):
    """ Product model """
    title = models.CharField(_('Title'), max_length=120)
    slug = models.CharField(_('Slug'), max_length=120, unique=True)
    specification = RichTextField(_('Specification'))
    price = models.IntegerField(_('Price'), null=True, blank=True)
    active = models.BooleanField(_('Active'), default=True)
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

    @staticmethod
    def get_absolute_url():
        return reverse('shop:main')

    @property
    def get_price(self):
        return self.price

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
