from django.contrib import admin

from apps.slider.models import Slider
from core.mixins.mixin import AdminBaseMixin


@admin.register(Slider)
class SliderAdmin(AdminBaseMixin):
    pass
