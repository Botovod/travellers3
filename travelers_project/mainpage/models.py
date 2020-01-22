from django.db import models


class MainPage(models.Model):
    main_banner = models.ImageField()
    big_description = models.CharField(max_length=255, default='', verbose_name='Большое описание')
    small_description = models.CharField(max_length=255, default='', verbose_name='Малое описание')
    link = models.CharField(max_length=255, default='', verbose_name='Ссылка')
    left_small_tile_title = models.CharField(
        max_length=255,
        default='',
        verbose_name='Заголовок маленькой левой плитки')
    left_small_tile_description = models.TextField(
        default='',
        blank=True,
        verbose_name='Описание маленькой левой плитки')
    center_small_tile_title = models.CharField(
        max_length=255,
        default='',
        verbose_name='Заголовок маленькой центральной плитки')
    center_small_tile_description = models.TextField(
        default='',
        blank=True,
        verbose_name='Описание маленькой центральной плитки')
    right_small_tile_title = models.CharField(
        max_length=255,
        default='',
        verbose_name='Заголовок маленькой правой плитки')
    right_small_tile_description = models.TextField(
        default='',
        blank=True,
        verbose_name='Описание маленькой правой плитки')
    video_link = models.CharField(max_length=255, default='', verbose_name='Видео')

    left_big_tile_header = models.CharField(
        max_length=255,
        default='',
        verbose_name='Большой заголовок большой левой плитки')
    left_big_tile_title = models.CharField(
        max_length=255,
        default='',
        verbose_name='Заголовок большой левой плитки')
    left_big_tile_description = models.TextField(
        default='',
        blank=True,
        verbose_name='Описание большой левой плитки')
    right_big_tile_header = models.CharField(
        max_length=255,
        default='',
        verbose_name='Большой заголовок большой правой плитки')
    right_big_tile_title = models.CharField(
        max_length=255,
        default='',
        verbose_name='Заголовок большой правой плитки')
    right_big_tile_description = models.TextField(
        default='',
        blank=True,
        verbose_name='Описание большой правой плитки')
