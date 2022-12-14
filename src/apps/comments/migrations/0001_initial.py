# Generated by Django 4.1.2 on 2022-11-17 21:56

import ckeditor_uploader.fields
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
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_seo', models.CharField(blank=True, max_length=500, null=True, verbose_name='Title Seo')),
                ('meta_keywords', models.TextField(blank=True, null=True, verbose_name='Keywords')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content')),
                ('to_model', models.CharField(blank=True, choices=[('Article', 'Article'), ('Comment', 'Comment'), ('Course', 'Course'), ('Product', 'Product')], default='Comment', max_length=20, verbose_name='Associated')),
                ('model_id', models.IntegerField(blank=True, default=0, verbose_name='To #')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Author id')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ('-created_at',),
            },
        ),
    ]
