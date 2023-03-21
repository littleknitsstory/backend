# Generated by Django 4.1.2 on 2023-03-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reactions", "0002_reaction_unique_reaction"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="reaction",
            name="unique_reaction",
        ),
        migrations.AddConstraint(
            model_name="reaction",
            constraint=models.UniqueConstraint(
                fields=("author", "model_type", "model_id", "reaction"),
                name="unique_reaction",
            ),
        ),
    ]
