# Generated by Django 4.1.2 on 2023-04-03 10:39

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import optimized_image.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("title", models.CharField(max_length=64, verbose_name="Title")),
                (
                    "title_ru",
                    models.CharField(max_length=64, null=True, verbose_name="Title"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=64, null=True, verbose_name="Title"),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        populate_from="title",
                        verbose_name="slug",
                    ),
                ),
                (
                    "meta_title",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="Title Seo"
                    ),
                ),
                (
                    "meta_title_ru",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="Title Seo"
                    ),
                ),
                (
                    "meta_title_en",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="Title Seo"
                    ),
                ),
                (
                    "meta_keywords",
                    models.TextField(blank=True, null=True, verbose_name="Keywords"),
                ),
                (
                    "meta_keywords_ru",
                    models.TextField(blank=True, null=True, verbose_name="Keywords"),
                ),
                (
                    "meta_keywords_en",
                    models.TextField(blank=True, null=True, verbose_name="Keywords"),
                ),
                (
                    "meta_description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "meta_description_ru",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "meta_description_en",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
            ],
            options={
                "verbose_name": "Tag",
                "verbose_name_plural": "Tags",
            },
        ),
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=64, verbose_name="Title")),
                (
                    "title_ru",
                    models.CharField(max_length=64, null=True, verbose_name="Title"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=64, null=True, verbose_name="Title"),
                ),
                (
                    "slug",
                    django_extensions.db.fields.AutoSlugField(
                        blank=True,
                        editable=False,
                        populate_from="title",
                        verbose_name="slug",
                    ),
                ),
                (
                    "content",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, verbose_name="Content"
                    ),
                ),
                (
                    "content_ru",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True, verbose_name="Content"
                    ),
                ),
                (
                    "content_en",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True, verbose_name="Content"
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
                (
                    "meta_title",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="Title Seo"
                    ),
                ),
                (
                    "meta_title_ru",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="Title Seo"
                    ),
                ),
                (
                    "meta_title_en",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="Title Seo"
                    ),
                ),
                (
                    "meta_keywords",
                    models.TextField(blank=True, null=True, verbose_name="Keywords"),
                ),
                (
                    "meta_keywords_ru",
                    models.TextField(blank=True, null=True, verbose_name="Keywords"),
                ),
                (
                    "meta_keywords_en",
                    models.TextField(blank=True, null=True, verbose_name="Keywords"),
                ),
                (
                    "meta_description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "meta_description_ru",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "meta_description_en",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "image_preview",
                    optimized_image.fields.OptimizedImageField(
                        blank=True, upload_to="", verbose_name="Images"
                    ),
                ),
                (
                    "image_alt",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Images Alt"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="article_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True,
                        related_name="article_tags",
                        to="blog.tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
                "ordering": ("-created_at",),
            },
        ),
    ]
