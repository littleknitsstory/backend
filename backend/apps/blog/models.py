from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django.template.defaultfilters import slugify
from core.mixin import SeoMixin, ImagesMixin
from apps.tags.models import Tag


class Article(SeoMixin, ImagesMixin):
    """ Article model """
    title = models.CharField(_('Title'), max_length=64)
    slug = models.SlugField(_('Slug'), max_length=256, unique=True)
    content = models.TextField(_('Content'))
    active = models.BooleanField(_('Active'), default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='article_user',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    tags = models.ManyToManyField(Tag, related_name='article_tags', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ('-created_at',)
