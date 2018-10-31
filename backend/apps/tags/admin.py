from django.contrib import admin
from apps.tags.models import Tag


@admin.register(Tag)  # noqa
class AdminTag(admin.ModelAdmin):  # noqa
    """
    tags
    """
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug')
    save_as = True
    save_on_top = True

