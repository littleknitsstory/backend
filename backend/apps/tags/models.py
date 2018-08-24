from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class Tag(models.Model):
    title = models.CharField(_('Title'), max_length=64)
    slug = models.SlugField(max_length=64, default="")
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Tag, self).save(*args, **kwargs)

