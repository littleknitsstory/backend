from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    title = models.CharField(_('Title'), max_length=120)
    image = models.ImageField(_('Image'), blank=True, null=True)
    image_alt = models.CharField(max_length=120, blank=True, null=True)
    slug = models.CharField(max_length=120, unique=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    keywords = models.CharField(_('Keywords'), max_length=120, null=True, blank=True)
    price = models.IntegerField(_('Price'), null=True, blank=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField('Category', related_name='products')
    tags = models.ManyToManyField('tags.Tag', related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title
