from django.contrib import admin
from src.apps.contacts.models import Contact


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "message", "created_at"]
    fields = ["name", "email", "message", "phone_number", "company"]
