from django.contrib import admin

from src.apps.slider.models import Slider
from src.core.mixins.mixin import AdminBaseMixin


@admin.register(Slider)
class SliderAdmin(AdminBaseMixin):
    pass
