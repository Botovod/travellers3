from django.db import models

from geography.models import City
from geography.models import Sight


class RouteByCities(models.Model):
    title = models.CharField(max_length=255, default='', verbose_name='Название маршрута')
    cities = models.ManyToManyField(City, blank=False, verbose_name='Города маршрута')

    class Meta:
        verbose_name = 'Маршрут по городам'
        verbose_name_plural = 'Маршруты по городам'

    def __str__(self):
        return self.title


class RouteBySights(models.Model):
    title = models.CharField(max_length=255, default='', verbose_name='Название маршрута')
    sights = models.ManyToManyField(Sight, blank=False, verbose_name='Достопримечательности маршрута')

    class Meta:
        verbose_name = 'Маршрут по достопримечательностям'
        verbose_name_plural = 'Маршруты по достопримечательностям'

    def __str__(self):
        return self.title
