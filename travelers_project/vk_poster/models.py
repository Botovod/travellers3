from django.db import models


class CityPost(models.Model):
    header = models.CharField(max_length=255, default='', verbose_name='Название конфигурации')
    region = models.BooleanField(default=True, verbose_name="Регион")
    title = models.BooleanField(default=True, verbose_name='Название')
    description = models.BooleanField(default=True, verbose_name='Описание')
    image = models.BooleanField(default=True, verbose_name='Изображение')
    latitude = models.BooleanField(verbose_name='Широта')
    longitude = models.BooleanField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Пост города'
        verbose_name_plural = 'Посты городов'

    def __str__(self):
        return self.header


class SightPost(models.Model):
    header = models.CharField(max_length=255, default='', verbose_name='Название конфигурации')
    city = models.BooleanField(default=True, verbose_name='Город')
    title = models.BooleanField(default=True, verbose_name='Название')
    text = models.BooleanField(default=True, verbose_name='Описание')
    image = models.BooleanField(default=True, verbose_name='Фотография достопримечательности')
    coordinates = models.BooleanField(verbose_name='Координаты')
    latitude = models.BooleanField(verbose_name='Широта')
    longitude = models.BooleanField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Пост достопримечательности'
        verbose_name_plural = 'Посты достопримечтельностей'

    def __str__(self):
        return self.header


class CityTripPost(models.Model):
    header = models.CharField(max_length=255, default='', verbose_name='Название конфигурации')
    title = models.BooleanField(verbose_name='Название путешествия')
    start_date = models.BooleanField(verbose_name='Дата начала путешествия')
    end_date = models.BooleanField(verbose_name='Дата окончания путешествия')
    description = models.BooleanField(verbose_name='Описание путешествия')
    traveler = models.BooleanField(verbose_name='Путешественники')
    route = models.BooleanField(verbose_name='Путешествие по маршрутам городов')

    class Meta:
        verbose_name = 'Пост путешествия городам'
        verbose_name_plural = 'Посты путешествий по городам'

    def __str__(self):
        return self.header
