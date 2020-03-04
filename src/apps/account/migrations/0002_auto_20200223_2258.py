# Generated by Django 3.0.2 on 2020-02-23 19:58

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_profile_full",
            field=models.BooleanField(default=False, verbose_name="Profile full"),
        ),
    ]