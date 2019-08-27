from django.contrib import admin
from apps.contacts.models import Subscribe
from apps.contacts.models import Feedback
from apps.contacts.models import Review


class SubscribeAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'created_at', 'hidden')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Subscribe, SubscribeAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'feedback', 'created_at']


admin.site.register(Feedback, FeedbackAdmin)


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('user_name', 'comment', 'created_at')
    list_filter = ['created_at', 'user_name']
    search_fields = ['comment']


admin.site.register(Review, ReviewAdmin)
