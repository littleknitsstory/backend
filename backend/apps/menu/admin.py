from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Menu, MenuItems

admin.site.register(Menu)

admin.site.register(MenuItems, MPTTModelAdmin)
