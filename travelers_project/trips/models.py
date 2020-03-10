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

    def __str__(self):
        return self.title


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

    @property
    def get_title(self):
        title = ''
        if self.title:
            title = f'{self.title}\n'
        return title

    @property
    def get_route(self):
        route = ''
        if self.route:
            route = f'Маршрут: {self.route}\n'
        return route

    @property
    def get_start_date(self):
        start_date = ''
        if self.start_date:
            start_date = f'Дата начала: {self.start_date.strftime("%d/%m/%Y")}\n'
        return start_date

    @property
    def get_end_date(self):
        end_date = ''
        if self.end_date:
            end_date = f'Дата окончания: {self.end_date.strftime("%d/%m/%Y")}\n'
        return end_date

    @property
    def get_description(self):
        description = ''
        if self.description:
            description = f'\n{self.description}'
        return description


class SightTrip(AbstractTrip):
    route = models.ForeignKey(
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
