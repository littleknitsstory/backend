from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class SeoMixin(models.Model):
    """
        Abstract model for basic seo information
        Attributes:
        description (text): description seo text field
        keywords (text): seo keywords
        title_seo (char): page's title_seo
        created_at: info created
        update_at: info update
    """
    title_seo = models.CharField(_("Title Seo"), max_length=500, null=True, blank=True)
    keywords = models.TextField(_("Keywords"), blank=True)
    description = models.TextField(_("Description"), blank=True)

    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    update_at = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        abstract = True


class ImagesMixin(models.Model):
    """
        Abstract model for basic images information
        Attributes:
        image_preview: path images
        image_alt (char): image_alt for <img>
    """
    image_preview = models.ImageField(_('Images'), blank=True)
    image_alt = models.CharField(_('Images Alt'), blank=True, max_length=255)

    class Meta:
        abstract = True


class AdminBaseMixin(admin.ModelAdmin):
    """ Abstract model for admin """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')
    save_as = True
    save_on_top = True

    class Meta:
        abstract = True
