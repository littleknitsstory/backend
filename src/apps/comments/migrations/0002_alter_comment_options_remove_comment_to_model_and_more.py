# Generated by Django 4.1.2 on 2023-03-07 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"verbose_name": "Comment", "verbose_name_plural": "Comments"},
        ),
        migrations.RemoveField(
            model_name="comment",
            name="to_model",
        ),
        migrations.AddField(
            model_name="comment",
            name="model_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ARTICLE", "Article"),
                    ("COMMENT", "Comment"),
                    ("COURSE", "Course"),
                    ("PRODUCT", "Product"),
                ],
                default="COMMENT",
                max_length=20,
                verbose_name="Model type",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Author",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="model_id",
            field=models.IntegerField(blank=True, default=0, verbose_name="Associated"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="text",
            field=models.CharField(max_length=263, verbose_name="Text"),
        ),
    ]
