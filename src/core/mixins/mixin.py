from django.db import models
from django.utils.translation import gettext_lazy as _
from optimized_image.fields import OptimizedImageField

# from src.core.utils.watermark import watermark_text
# TODO: разнести по файлам


class SeoMixin(models.Model):
    """
    Abstract model for basic seo information
    Attributes:
    description (text): description seo text field
    keywords (text): seo keywords
    title_seo (char): page's title_seo
    created_at: info created
    updated_at: info update
    """

    title_seo = models.CharField(_("Title Seo"), max_length=500, blank=True, null=True)
    meta_keywords = models.TextField(_("Keywords"), blank=True, null=True)
    meta_description = models.TextField(_("Description"), blank=True, null=True)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        abstract = True


class ImagesMixin(models.Model):
    """
    Abstract model for basic images information
    Attributes:
    image_preview: path images
    image_alt (char): image_alt for <img>
    """

    image_preview = OptimizedImageField(_("Images"), blank=True)
    image_alt = models.CharField(_("Images Alt"), blank=True, max_length=255)

    class Meta:
        abstract = True

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super(ImagesMixin, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )
        # TODO: watermark_text(self.image_preview.path, self.image_preview.path)

    def get_image(self) -> str:
        try:
            image = self.image_preview.url
        except ValueError:
            image = None
        return image
