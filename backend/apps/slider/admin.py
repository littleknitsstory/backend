from django.contrib import admin

from apps.slider.models import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')
    save_as = True
    save_on_top = True
