# Generated by Django 2.1.2 on 2018-11-02 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0002_auto_20181102_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_seo', models.CharField(blank=True, max_length=500, null=True, verbose_name='Title')),
                ('keywords', models.TextField(blank=True, null=True, verbose_name='Keywords')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('title', models.CharField(max_length=64, verbose_name='Title')),
                ('slug', models.SlugField(default='', max_length=256)),
                ('content', models.TextField(verbose_name='Content')),
                ('active', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='Active')),
                ('image_preview', models.ImageField(blank=True, upload_to='')),
                ('image_alt', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_user', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='tags', to='tags.Tag')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ImagesMixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
