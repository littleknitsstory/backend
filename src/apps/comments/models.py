from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from src.apps.comments.choices import CommentAssociationChoices


class Comment(models.Model):
    """Comment model.
    Basic seo information
    Attributes:
    description (text): description seo text field
    keywords (text): seo keywords
    title_seo (char): page's title_seo
    created_at: info created
    updated_at: info update.
    """

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="comments",
        on_delete=models.CASCADE,
        verbose_name=_("Author"),
    )
    text = models.CharField(_("Text"), max_length=263)
    model_type: CommentAssociationChoices = models.CharField(
        _("Model type"),
        choices=CommentAssociationChoices.MODEL_CHOICES,
        blank=True,
        default=CommentAssociationChoices.COMMENT,
        max_length=20,
    )
    model_id = models.IntegerField(_("Associated"), blank=True, default=0)
    is_deleted = models.BooleanField(_("Deleted"), default=False)
    meta_title = models.CharField(_("Title Seo"), max_length=500, blank=True, null=True)
    meta_keywords = models.TextField(_("Keywords"), blank=True, null=True)
    meta_description = models.TextField(_("Description"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return f"#{self.pk} by {self.author}"

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
