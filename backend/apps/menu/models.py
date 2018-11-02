from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _


class Menu(models.Model):
    """
    категории меню
    """
    STATUS = (
        (0, 'Активен'),
        (1, 'Не активен')
    )
    slug = models.CharField(max_length=100, verbose_name=_('Slug'), unique=True)
    hint = models.CharField(max_length=100, verbose_name=_('Hint'))
    active = models.BooleanField()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = _('Type')
        verbose_name_plural = _('Types')


class MenuItems(MPTTModel):
    """
    Элементы категории меню
    """
    STATUS = (
        (0, 'Активен'),
        (1, 'Не активен')
    )
    LINK_TARGET_CHOICES = (
        ('_blank', '_blank'),
        ('_top', '_top'),
        ('_parent', '_parent'),
    )
    name = models.CharField(max_length=200, verbose_name=_('Name'), default='')
    url = models.CharField(max_length=200, verbose_name=_('Link'))
    menu = models.ForeignKey(Menu, related_name='menu', verbose_name=_('Menu type'))
    target = models.CharField(max_length=10, choices=LINK_TARGET_CHOICES, null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    ordering = models.IntegerField(default=0, verbose_name=_('Sort'))
    status = models.IntegerField(default=0, choices=STATUS)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Menu item')
        verbose_name_plural = _('Menu items')
