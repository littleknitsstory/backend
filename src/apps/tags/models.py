from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

import core.mixins.mixin


class Tag(core.mixins.mixin.SeoMixin):
    """ Tag model """
    title = models.CharField(_('Title'), max_length=64)
    slug = models.SlugField(_('Slug'), max_length=64, unique=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)
