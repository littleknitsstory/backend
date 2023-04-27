from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from optimized_image.fields import OptimizedImageField


class Tag(models.Model):
    """Tag model"""

    title = models.CharField(_("Title"), max_length=64)
    slug = AutoSlugField(_("slug"), populate_from="title", editable=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.title


class Article(models.Model):
    """Article model"""

    title = models.CharField(_("Title"), max_length=64)
    description = models.CharField(_("Description"), max_length=63, null=True)
    slug = AutoSlugField(_("slug"), populate_from="title", editable=True)
    content = RichTextUploadingField(_("Content"), blank=True, config_name="default")
    is_active = models.BooleanField(_("Active"), default=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="article_user",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name=_("Author"),
    )
    tags = models.ManyToManyField(
        Tag, related_name="article_tags", blank=True, verbose_name=_("Tags")
    )
    meta_title = models.CharField(_("Title Seo"), max_length=500, blank=True, null=True)
    meta_keywords = models.TextField(_("Keywords"), blank=True, null=True)
    meta_description = models.TextField(_("Description"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    image_preview = OptimizedImageField(_("Images"), blank=True)
    image_alt = models.CharField(_("Images Alt"), blank=True, max_length=255)

    def __str__(self):
        return self.title

    def get_image(self) -> str:
        try:
            image = self.image_preview.url
        except ValueError:
            image = None
        return image

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ("-created_at",)
