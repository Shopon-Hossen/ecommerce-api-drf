# Generated by Django 5.1.7 on 2025-03-28 15:26

import django.contrib.postgres.indexes
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_shop_shop_shop_name_336728_gin'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddIndex(
            model_name='shop',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name'], name='shop_name_gin_idx', opclasses=['gin_trgm_ops']),
        ),
    ]
