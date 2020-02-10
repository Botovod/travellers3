# Generated by Django 2.2.7 on 2020-01-22 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_banner', models.ImageField(upload_to='')),
                ('big_description', models.CharField(default='', max_length=255, verbose_name='Большое описание')),
                ('small_description', models.CharField(default='', max_length=255, verbose_name='Малое описание')),
                ('link', models.CharField(default='', max_length=255, verbose_name='Ссылка')),
                ('left_small_tile_title', models.CharField(default='', max_length=255, verbose_name='Заголовок маленькой левой плитки')),
                ('left_small_tile_description', models.TextField(blank=True, default='', verbose_name='Описание маленькой левой плитки')),
                ('center_small_tile_title', models.CharField(default='', max_length=255, verbose_name='Заголовок маленькой центральной плитки')),
                ('center_small_tile_description', models.TextField(blank=True, default='', verbose_name='Описание маленькой центральной плитки')),
                ('right_small_tile_title', models.CharField(default='', max_length=255, verbose_name='Заголовок маленькой правой плитки')),
                ('right_small_tile_description', models.TextField(blank=True, default='', verbose_name='Описание маленькой правой плитки')),
                ('video_link', models.CharField(default='', max_length=255, verbose_name='Видео')),
                ('left_big_tile_header', models.CharField(default='', max_length=255, verbose_name='Большой заголовок большой левой плитки')),
                ('left_big_tile_title', models.CharField(default='', max_length=255, verbose_name='Заголовок большой левой плитки')),
                ('left_big_tile_description', models.TextField(blank=True, default='', verbose_name='Описание большой левой плитки')),
                ('right_big_tile_header', models.CharField(default='', max_length=255, verbose_name='Большой заголовок большой правой плитки')),
                ('right_big_tile_title', models.CharField(default='', max_length=255, verbose_name='Заголовок большой правой плитки')),
                ('right_big_tile_description', models.TextField(blank=True, default='', verbose_name='Описание большой правой плитки')),
            ],
        ),
    ]