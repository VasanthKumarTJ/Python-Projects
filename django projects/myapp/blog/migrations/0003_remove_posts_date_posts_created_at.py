# Generated by Django 5.1.7 on 2025-03-25 18:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_posts_img_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='date',
        ),
        migrations.AddField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
