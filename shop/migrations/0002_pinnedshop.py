# Generated by Django 5.1.7 on 2025-03-29 07:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PinnedShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pinned_by_users', to='shop.shop')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pinned_shop', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'shop')},
            },
        ),
    ]
