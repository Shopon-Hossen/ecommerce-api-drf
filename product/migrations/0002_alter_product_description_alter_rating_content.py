# Generated by Django 5.2 on 2025-04-17 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
