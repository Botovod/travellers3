# Generated by Django 2.2.7 on 2020-03-09 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.BooleanField(default=True, verbose_name='Регион')),
                ('title', models.BooleanField(default=True, verbose_name='Название')),
                ('description', models.BooleanField(default=True, verbose_name='Описание')),
                ('image', models.BooleanField(default=True, verbose_name='Изображение')),
                ('latitude', models.BooleanField(verbose_name='Широта')),
                ('longitude', models.BooleanField(verbose_name='Долгота')),
            ],
            options={
                'verbose_name': 'Пост города',
                'verbose_name_plural': 'Посты городов',
            },
        ),
    ]
