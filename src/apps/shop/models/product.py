import logging

from colorful.fields import RGBColorField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

from src.core.mixins.mixin import SeoMixin, ImagesMixin

logger = logging.getLogger(__name__)
User = get_user_model()


class Product(SeoMixin, ImagesMixin):
    title = models.CharField(_("Title"), max_length=120)
    code = models.IntegerField(verbose_name=_("Code product"), db_index=True)
    slug = AutoSlugField(_("slug"), populate_from="title", editable=True)
    is_active = models.BooleanField(_("Active"), default=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    price = models.DecimalField(
        _("Price"),
        null=False,
        blank=True,
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    sale = models.DecimalField(
        _("Sale"),
        null=False,
        blank=True,
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    currency = models.CharField(_("Currency"), default="EUR", max_length=3)
    count = models.IntegerField(verbose_name=_("Count"), blank=True, default=1)
    type_product = models.CharField(
        _("Type Product"), max_length=120, null=True, blank=True
    )
    material = models.CharField(_("Material"), max_length=120, null=True, blank=True)
    included = models.CharField(_("Included"), max_length=120, null=True, blank=True)
    height = models.IntegerField(_("Height"), null=True, blank=True)
    weight = models.IntegerField(_("Weight"), null=True, blank=True)

    is_shipping_required = models.BooleanField(default=True)
    is_digital = models.BooleanField(default=False)

    colors = models.ManyToManyField(
        "ProductColor",
        verbose_name=_("Colors"),
        related_name="product_colors",
        blank=True,
    )
    categories = models.ManyToManyField(
        "Category",
        verbose_name=_("Category"),
        related_name="product_categories",
        blank=True,
    )
    author = models.ForeignKey(
        User,
        related_name="product_author",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.title}"

    def __repr__(self) -> str:
        class_ = type(self)
        return (
            f"<{class_.__module__}.{class_.__name__}"
            f"(code={self.code}, name={self.title})>"
        )


class ProductPhoto(ImagesMixin):
    product = models.ForeignKey(
        "Product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name="photo_product",
    )

    class Meta:
        verbose_name = _("Product photo")
        verbose_name_plural = _("Product photos")

    def __str__(self):
        return f"{self.product}"


class ProductColor(models.Model):
    color = RGBColorField(verbose_name=_("Color"))

    class Meta:
        verbose_name = _("Product color")
        verbose_name_plural = _("Product colors")

    def __str__(self):
        return f"{self.color}"


class ProductSimilar(models.Model):
    product = models.ForeignKey(
        "Product",
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name="similar_product",
    )
    products = models.ManyToManyField(
        "Product", verbose_name=_("Products"), related_name="similar_products"
    )

    class Meta:
        verbose_name = (_("Product Similar"),)
        verbose_name_plural = _("Products Similar")

    def __str__(self):
        return f"{self.product}"
