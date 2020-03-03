from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Menu, MenuItems


@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    list_display = ("slug", "hint", "is_active")


@admin.register(MenuItems)
class AdminMenuItems(MPTTModelAdmin):
    list_display = ("name", "menu", "url", "target", "parent", "ordering", "is_active")
    search_fields = ("name",)
    list_editable = ("ordering", "is_active")
    list_filter = ("menu",)
    save_as = True
    save_on_top = True
