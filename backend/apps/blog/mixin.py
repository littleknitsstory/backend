from django.db import models
from django.utils.translation import ugettext_lazy as _


class SeoMixin(models.Model):
    """Abstract model for basic seo information
    Attributes:
    description (text): description seo text field
    header (text): page's header text
    keywords (text): seo keywords
    title_seo (char): page's title_seo
    """
    title_seo = models.CharField(_("Title"), max_length=500, blank=True, null=True)
    keywords = models.TextField(_("Keywords"), blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        abstract = True


class ImagesMixin(models.Model):
    pass
    # image_preview = models.ImageField(blank=True)
    # image_alt = models.CharField(blank=True, max_length=255)
