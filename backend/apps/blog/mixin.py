from django.db import models


class SeoMixin(models.Model):
    """Abstract model for basic seo information
    Attributes:
        description (text): description seo text field
        header (text): page's header text
        keywords (text): seo keywords
        title (char): page's title
    """
    # title = models.CharField(max_length=500, verbose_name=_("Title"), blank=True, null=True)
    # header = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class ImagesMixin(models.Model):
    pass
    # image_preview = models.ImageField(blank=True)
    # image_alt = models.CharField(blank=True, max_length=255)
