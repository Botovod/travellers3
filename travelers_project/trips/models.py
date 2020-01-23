from django.db import models
from traces.models import RouteByCities, RouteBySights


class Traveler(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')

    class Meta:
        verbose_name = 'Путешественник'
        verbose_name_plural = 'Путешественники'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Trip(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название путешествия')
    start_date = models.DateField(verbose_name='Дата начала путешествия')
    end_date = models.DateField(verbose_name='Дата окончания путешествия')
    description = models.TextField(default='', verbose_name='Описание путешествия')
    traveler = models.ManyToManyField(Traveler, related_name='trip_traveler', verbose_name='Путешественники')
    route_by_sights = models.ManyToManyField(
        RouteBySights,
        related_name='trip_route_sight',
        verbose_name='Путешествие по маршрутам достопримечательностей')
    route_by_cities = models.ManyToManyField(
        RouteByCities,
        related_name='trip_route_city',
        verbose_name='Путешествие по маршрутам городов')

    class Meta:
        verbose_name = 'Путешествие'
        verbose_name_plural = 'Путешествия'
        ordering = ['title']

    def __str__(self):
        return self.title
