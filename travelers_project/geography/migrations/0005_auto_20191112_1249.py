# Generated by Django 2.2.6 on 2019-11-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0004_city_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='sight',
            name='rating',
            field=models.SmallIntegerField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AddField(
            model_name='sightphoto',
            name='rating',
            field=models.SmallIntegerField(default=0, verbose_name='Рейтинг'),
        ),
    ]
