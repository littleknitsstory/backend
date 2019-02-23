from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.urls import reverse_lazy

from django.template.defaultfilters import slugify
from core.mixins.mixin import SeoMixin, ImagesMixin
from apps.tags.models import Tag


class Article(SeoMixin, ImagesMixin):
    """ Article model """
    title = models.CharField(_('Title'), max_length=64)
    slug = models.SlugField(_('Slug'), max_length=256, unique=True)
    content = RichTextField(_('Content'))
    is_active = models.BooleanField(_('Active'), default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='article_user',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    tags = models.ManyToManyField(Tag, related_name='article_tags', blank=True)

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse_lazy('blog:blog-list')

    @property
    def get_custom_url(self):
        return reverse_lazy('blog:blog-detail', kwargs={'slug': self.slug})

    @property
    def get_app_name(self):
        return 'Блог'

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ('-created_at',)
