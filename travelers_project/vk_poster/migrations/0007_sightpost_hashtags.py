# Generated by Django 2.2.7 on 2020-03-10 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vk_poster', '0006_citypost_hashtags'),
    ]

    operations = [
        migrations.AddField(
            model_name='sightpost',
            name='hashtags',
            field=models.BooleanField(default=True, verbose_name='Хэштэги'),
        ),
    ]