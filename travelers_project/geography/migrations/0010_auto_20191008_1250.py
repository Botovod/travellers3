# Generated by Django 2.2.5 on 2019-10-08 12:50

from django.db import migrations, models
import geography.models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0009_auto_20191008_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightphoto',
            name='file',
            field=models.ImageField(default='', max_length=200, upload_to=geography.models.image_sight, verbose_name='Изображение'),
        ),
    ]