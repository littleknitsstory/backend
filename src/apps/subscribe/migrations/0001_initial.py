# Generated by Django 4.1.2 on 2023-04-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subscribe",
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
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                (
                    "hidden",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Hidden"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created_at"),
                ),
            ],
            options={
                "verbose_name": "Subscriber",
                "verbose_name_plural": "Subscribers",
            },
        ),
    ]
