from django.db import models
from typing import Optional
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
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    status = models.CharField(
        verbose_name=_("Status"),
        choices=OrderCartStatusChoices.CHOICES,
        default=OrderCartStatusChoices.NEW,
        max_length=14,
    )
    order_total_cost = models.DecimalField(
        _("Total cost order"),
        null=False,
        blank=True,
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    currency = models.CharField(_("Currency"), default="EUR", max_length=3)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.order_number}-{self.order_total_cost}"

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


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
    item_total_cost = models.DecimalField(
        _("Total cost item order"),
        null=False,
        blank=True,
        max_digits=14,
        decimal_places=2,
        default=0,
    )
    currency = models.CharField(_("Currency"), default="EUR", max_length=3)

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"{self.product} - {self.amount}"

    def get_and_save_total_cost_item(self):
        self.item_total_cost = self.product.price * self.amount
        self.save()
        return self.item_total_cost

    @property
    def is_digital(self) -> Optional[bool]:
        """Check if a variant is digital and contains digital content."""
        if not self.product:
            return None
        is_digital = self.product.is_digital()
        has_digital = hasattr(self.product, "digital_content")
        return is_digital and has_digital
