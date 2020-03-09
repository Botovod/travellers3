# Generated by Django 2.2.7 on 2020-03-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vk_poster', '0004_auto_20200309_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityTripPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(default='', max_length=255, verbose_name='Название конфигурации')),
                ('title', models.BooleanField(verbose_name='Название путешествия')),
                ('start_date', models.BooleanField(verbose_name='Дата начала путешествия')),
                ('end_date', models.BooleanField(verbose_name='Дата окончания путешествия')),
                ('description', models.BooleanField(verbose_name='Описание путешествия')),
                ('traveler', models.BooleanField(verbose_name='Путешественники')),
                ('route', models.BooleanField(verbose_name='Путешествие по маршрутам городов')),
            ],
            options={
                'verbose_name': 'Пост путешествия городам',
                'verbose_name_plural': 'Посты путешествий по городам',
            },
        ),
    ]
