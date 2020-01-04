from django.contrib import admin
from .models import Menu, MenuItems
from django_mptt_admin.admin import DjangoMpttAdmin


@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    list_display = ('slug', 'hint', 'active')


@admin.register(MenuItems)
class AdminMenuItems(DjangoMpttAdmin):
    list_display = ('name', 'menu', 'url', 'target', 'parent', 'ordering', 'is_active')
    search_fields = ('name',)
    list_editable = ('ordering', 'is_active')
    list_filter = ('menu',)
    save_as = True
    save_on_top = True
