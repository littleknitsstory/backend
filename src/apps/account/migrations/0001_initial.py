# Generated by Django 3.1 on 2020-08-14 15:08

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import django_countries.fields
import optimized_image.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "account_type",
                    models.CharField(
                        choices=[
                            ("AUTHOR", "Author"),
                            ("MANAGER", "Manager"),
                            ("CLIENT", "Client"),
                        ],
                        default="CLIENT",
                        max_length=63,
                        verbose_name="Type user",
                    ),
                ),
                (
                    "avatar",
                    optimized_image.fields.OptimizedImageField(
                        blank=True, null=True, upload_to="", verbose_name="Avatar"
                    ),
                ),
                (
                    "about",
                    models.TextField(
                        blank=True,
                        max_length=633,
                        null=True,
                        verbose_name="About author",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=13,
                        null=True,
                        verbose_name="Phone number",
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(
                        blank=True,
                        default=None,
                        max_length=2,
                        null=True,
                        verbose_name="Country",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=63, null=True, verbose_name="City"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=512, null=True, verbose_name="Address"
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(blank=True, null=True, verbose_name="Birth date"),
                ),
                (
                    "is_email_confirmed",
                    models.BooleanField(default=False, verbose_name="Email confirm"),
                ),
                (
                    "is_profile_full",
                    models.BooleanField(default=False, verbose_name="Profile full"),
                ),
                (
                    "vk_profile",
                    models.JSONField(blank=True, null=True, verbose_name="Vk profile"),
                ),
                (
                    "fb_profile",
                    models.JSONField(blank=True, null=True, verbose_name="Fb profile"),
                ),
                (
                    "inst_profile",
                    models.JSONField(
                        blank=True, null=True, verbose_name="Instagram profile"
                    ),
                ),
                (
                    "tg_profile",
                    models.JSONField(
                        blank=True, null=True, verbose_name="Telegram profile"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
