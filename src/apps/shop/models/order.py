from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import ShortUUIDField

from src.apps.shop.choices import OrderCartStatusChoices


class OrderCart(models.Model):
    order_number = ShortUUIDField(_("Number order"))
    address = models.CharField(
        verbose_name=_("Address"), max_length=256, null=True, blank=True
    )
    phone = models.CharField(
        verbose_name=_("Phone"), max_length=13, null=True, blank=True
    )
    email = models.EmailField(verbose_name=_("Email"), null=True, blank=True)
    comments = models.CharField(
        verbose_name=_("Comments"), max_length=512, null=True, blank=True
    )
    created_at = models.DateTimeField(verbose_name=_("Created"), auto_now_add=True)
    update_at = models.DateTimeField(_("Updated at"), auto_now=True)
    status = models.CharField(
        verbose_name=_("Status"),
        choices=OrderCartStatusChoices.CHOICES,
        default=OrderCartStatusChoices.NEW,
        max_length=14,
    )
    products = ""

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.id}"


class OrderCartItem(models.Model):
    order_cart = models.ForeignKey(
        "OrderCart",
        on_delete=models.CASCADE,
        verbose_name=_("Order Cart"),
        related_name="ordercartitem_ordercart",
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        verbose_name=_("Product"),
        related_name="ordercartitem_product",
    )
    amount = models.PositiveSmallIntegerField(verbose_name=_("Amount"), default=0)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"{self.product} - {self.amount}"
