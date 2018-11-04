from django.contrib import admin
from .models import Subscribe

class SubscribeAdmin(admin.ModelAdmin):

    readonly_fields = ('email', 'created', 'hidden')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Subscribe, SubscribeAdmin)
