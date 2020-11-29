from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from src.apps.slider.models import Slider


@admin.register(Slider)
class SliderAdmin(TranslationAdmin):
    save_as = True
    save_on_top = True
    list_display = ("title", "slug", "is_active")
    fieldsets = (
        (_("Title"), {"fields": ("title", "sub_title")}),
        (
            _("Main"),
            {"fields": ("slug", "link", "ordering", "image_preview", "image_alt")},
        ),
    )
