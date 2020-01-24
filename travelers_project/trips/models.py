from django.db import models
from traces.models import RouteByCities, RouteBySights
from django.contrib.auth.models import User


class Traveler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    birth_date = models.DateTimeField(verbose_name='Дата рождения')

    class Meta:
        verbose_name = 'Путешественник'
        verbose_name_plural = 'Путешественники'

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'


class AbstractTrip(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название путешествия')
    start_date = models.DateTimeField(verbose_name='Дата начала путешествия')
    end_date = models.DateTimeField(verbose_name='Дата окончания путешествия')
    description = models.TextField(default='', verbose_name='Описание путешествия')
    traveler = models.ManyToManyField(Traveler, verbose_name='Путешественники')

    class Meta:
        abstract = True


class CityTrip(AbstractTrip):
    route = models.ForeignKey(
        RouteByCities,
        on_delete=models.DO_NOTHING,
        related_name='trip_route_city',
        blank=True,
        null=True,
        verbose_name='Путешествие по маршрутам городов')

    class Meta:
        verbose_name = 'Путешествие городам'
        verbose_name_plural = 'Путешествия по городам'
        ordering = ['title']

    def __str__(self):
        return self.title


class SightTrip(AbstractTrip):
    route_by_sights = models.ForeignKey(
        RouteBySights,
        on_delete=models.DO_NOTHING,
        related_name='trip_route_sight',
        blank=True,
        null=True,
        verbose_name='Путешествие по маршрутам достопримечательностей')

    class Meta:
        verbose_name = 'Путешествие по достопримечательностям'
        verbose_name_plural = 'Путешествия по достопримечательностям'
        ordering = ['title']

    def __str__(self):
        return self.title
