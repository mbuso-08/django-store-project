# Generated by Django 4.2.6 on 2023-11-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_item_description_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
