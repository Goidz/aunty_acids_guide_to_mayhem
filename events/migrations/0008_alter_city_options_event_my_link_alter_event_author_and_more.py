# Generated by Django 5.0.6 on 2024-06-06 10:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_alter_venue_created_on'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name', '-created_on']},
        ),
        migrations.AddField(
            model_name='event',
            name='my_link',
            field=models.URLField(default=0, verbose_name='Add a Website'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.TextField(max_length=100, unique=True),
        ),
    ]
