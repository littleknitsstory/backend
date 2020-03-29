from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django_extensions.db.fields import AutoSlugField
from django_extensions.db.models import TitleSlugDescriptionModel
from djmoney.models.fields import MoneyField

from colorful.fields import RGBColorField
from ckeditor.fields import RichTextField

from src.core.mixins.mixin import SeoMixin, ImagesMixin


class Product(SeoMixin, ImagesMixin):
    title = models.CharField(_("Title"), max_length=120)
    code = models.IntegerField(verbose_name=_("Code product"))
    slug = AutoSlugField(_('slug'), populate_from='title', editable=True)
    is_active = models.BooleanField(_("Active"), default=True)
    description = RichTextField(_("Description"))
    price = MoneyField(
        _("Price"),
        null=True,
        blank=True,
        max_digits=14,
        decimal_places=2,
        default_currency="RUB",
    )
    sale = MoneyField(
        _("Sale"),
        null=True,
        blank=True,
        max_digits=14,
        decimal_places=2,
        default_currency="RUB",
    )
    count = models.IntegerField(verbose_name=_("Count"), blank=True, default=1)
    type_product = models.CharField(
        _("Type Product"), max_length=120, null=True, blank=True
    )
    material = models.CharField(_("Material"), max_length=120, null=True, blank=True)
    included = models.CharField(_("Included"), max_length=120, null=True, blank=True)
    height = models.IntegerField(_("Height"), null=True, blank=True)
    weight = models.IntegerField(_("Weight"), null=True, blank=True)
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
        settings.AUTH_USER_MODEL,
        related_name="product_author",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    @property
    def get_price(self):
        return self.price


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
