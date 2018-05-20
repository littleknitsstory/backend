import datetime
import uuid # for unique slug

from django.db import models
from blog.mixin import SeoMixin

# Generate unique slug
from django.db.models import permalink
from django.template.defaultfilters import slugify


def unique_slug(title):
    uniqueid = uuid.uuid1().hex[:5]
    slug = slugify(title) + "-" + str(uniqueid)

    if not PostModel.objects.filter(slug=slug).exists():
        # If there's no posts with such slug,
        # then the slug is unique, so I return it
        return slug
    else:
        # If the post with this slug already exists -
        # I try to generate unique slug again
        return unique_slug(title)


class PostModel(SeoMixin, models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=256, default="")
    content = models.TextField(default="", null=True, blank=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    image_preview = models.ImageField(blank=True)
    image_alt = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.title

    def save(self, slug="", *args, **kwargs):
        if not self.id:
            self.pub_date = datetime.datetime.now()
            self.slug = unique_slug(self.title)
    
        return super(PostModel, self).save(*args, **kwargs)

    @permalink
    def get_absolute_url(self):
        return ('post_detail', None, {'slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-pub_date',)
