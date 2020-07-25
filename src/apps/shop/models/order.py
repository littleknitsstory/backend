from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import ShortUUIDField
from djmoney.contrib.exchange.models import convert_money
from djmoney.models.fields import MoneyField

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
    order_total_cost = MoneyField(
        _("Total cost order"),
        null=False,
        blank=True,
        max_digits=14,
        decimal_places=2,
        default_currency="RUB",
        default=0,
    )
    # FIXME: del this
    products = ""

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.order_number}-{self.order_total_cost}"

    def get_total_cost_order(self):
        order_total_cost = self.order_total_cost
        items = self.ordercartitem_ordercart.all()
        for item in items:
            if item.item_total_cost is not None:
                order_total_cost = convert_money(
                    order_total_cost, "RUB"
                ) + convert_money(item.item_total_cost, "RUB")
        return order_total_cost


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
    item_total_cost = MoneyField(
        _("Total cost item order"),
        null=False,
        blank=True,
        max_digits=14,
        decimal_places=2,
        default_currency="RUB",
        default=0,
    )

    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

    def __str__(self):
        return f"{self.product} - {self.amount}"

    def save(self, *args, **kwargs):
        self.item_total_cost = self.get_total_cost_item()
        super().save(*args, **kwargs)

    def get_total_cost_item(self):
        if self.amount == 0:
            return self.product.price
        return self.product.price * self.amount
