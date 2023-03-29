# Generated by Django 4.1.2 on 2023-03-23 08:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_article_content_alter_article_content_en_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=ckeditor.fields.RichTextField(blank=True, verbose_name="Content"),
        ),
        migrations.AlterField(
            model_name="article",
            name="content_en",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="Content"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="content_ru",
            field=ckeditor.fields.RichTextField(
                blank=True, null=True, verbose_name="Content"
            ),
        ),
    ]