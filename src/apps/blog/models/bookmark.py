from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.blog.models.models import Article

User = get_user_model()


class Bookmark(models.Model):
    """Bookmark model"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookmarks",
        verbose_name=_("User"),
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="bookmarks",
        verbose_name=_("Article"),
    )
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Bookmark")
        verbose_name_plural = _("Bookmarks")
        unique_together = (
            "user",
            "article",
        )

    def __str__(self):
        return f"{self.user} - {self.article}"
