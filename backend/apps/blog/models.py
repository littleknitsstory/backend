import datetime
import uuid # for unique slug

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


from apps.blog.mixin import SeoMixin

# Generate unique slug
from django.template.defaultfilters import slugify

from apps.tags.models import Tag


def unique_slug(title):
    uniqueid = uuid.uuid1().hex[:5]
    slug = slugify(title) + "-" + str(uniqueid)

    if not Article.objects.filter(slug=slug).exists():
        # If there's no posts with such slug,
        # then the slug is unique, so I return it
        return slug
    else:
        # If the post with this slug already exists -
        # I try to generate unique slug again
        return unique_slug(title)


class Article(SeoMixin, models.Model):
    
    ENABLED = (
        (0, _('Inactive')),
        (1, _('Active')),
    )
    
    title = models.CharField(_('Title'), max_length=64)
    slug = models.SlugField(max_length=256, default='')
    content = models.TextField(_('Content'))
    active = models.IntegerField(_('Active'), default=1, choices=ENABLED)
    
    image_preview = models.ImageField(blank=True)
    image_alt = models.CharField(blank=True, max_length=255)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='article_user',
                               on_delete=models.CASCADE)
    
    tags = models.ManyToManyField(Tag, related_name='tags')
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('-created_at',)

