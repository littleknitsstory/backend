from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from django_extensions.db.fields import AutoSlugField
from src.core.mixins.mixin import SeoMixin, ImagesMixin


class Tag(SeoMixin):
    """ Tag model """

    title = models.CharField(_("Title"), max_length=64)
    slug = AutoSlugField(_("slug"), populate_from="title", editable=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.title


class Article(SeoMixin, ImagesMixin):
    """ Article model """

    title = models.CharField(_("Title"), max_length=64)
    slug = AutoSlugField(_("slug"), populate_from="title", editable=True)
    content = RichTextUploadingField(_("Content"))
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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ("-created_at",)
