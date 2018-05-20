from django.contrib import admin

from blog.models import PostModel


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
