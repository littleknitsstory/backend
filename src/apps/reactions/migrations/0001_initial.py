# Generated by Django 4.1.2 on 2023-03-16 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Reaction",
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
                (
                    "model_type",
                    models.CharField(
                        blank=True,
                        choices=[("ARTICLE", "Article"), ("COMMENT", "Comment")],
                        default="ARTICLE",
                        max_length=20,
                        verbose_name="Model type",
                    ),
                ),
                (
                    "model_id",
                    models.IntegerField(
                        blank=True, default=0, verbose_name="Associated"
                    ),
                ),
                (
                    "reaction",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("RED_HEART", "RED HEART"),
                            ("FIRE", "FIRE"),
                            ("SMILING", "SMILING"),
                            ("THUMBS UP", "THUMBS UP"),
                            ("DEFAULT", "DEFAULT"),
                        ],
                        default="RED_HEART",
                        max_length=20,
                        verbose_name="Reaction_type",
                    ),
                ),
                (
                    "is_delete",
                    models.BooleanField(default=False, verbose_name="Deleted"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reactions",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author",
                    ),
                ),
            ],
            options={
                "verbose_name": "Reaction",
                "verbose_name_plural": "Reactions",
            },
        ),
    ]
