# Generated by Django 5.1.7 on 2025-03-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopreview',
            name='comment',
            field=models.TextField(),
        ),
    ]
