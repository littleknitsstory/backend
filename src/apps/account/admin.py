from django.contrib import admin

from src.apps.account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'username', 'email')
	fields = (
		'username', 'first_name', 'last_name', 'email', 'date_joined', 'account_type', 'avatar',
		'about', 'phone_number', 'country', 'city', 'birth_date', 'is_email_confirmed', 'is_profile_full',
		'vk_profile', 'fb_profile', 'inst_profile', 'tg_profile'
	)
