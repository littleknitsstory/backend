from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from src.apps.slider.models import Slider
from src.core.mixins.mixin import AdminBaseMixin


@admin.register(Slider)
class SliderAdmin(TranslationAdmin, AdminBaseMixin):
    list_display = ("title", "slug", "is_active")
    fieldsets = (
        (_("Title"), {"fields": ("title", "sub_title")}),
        (
            _("Main"),
            {"fields": ("slug", "link", "ordering", "image_preview", "image_alt")},
        ),
    )
