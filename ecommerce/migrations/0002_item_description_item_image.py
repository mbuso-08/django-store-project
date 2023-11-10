# Generated by Django 4.2.6 on 2023-11-03 16:30

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='item description in here', max_length=250),
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='commerce'),
        ),
    ]
