from django.db import models
from django.contrib.postgres.fields import ArrayField

from geography.models import City
from geography.models import Sight


class RouteByCities(models.Model):
    title = models.CharField(max_length=255, default='', verbose_name='Название маршрута')
    cities = models.ManyToManyField(City, through='CitiesRelationship')

    class Meta:
        verbose_name = 'Маршрут по городам'
        verbose_name_plural = 'Маршруты по городам'

    def __str__(self):
        return self.title


class CitiesRelationship(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    route = models.ForeignKey(RouteByCities, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    def __str__(self):
        return '{}-{}'.format(self.route.title, self.city.title)


class RouteBySights(models.Model):
    title = models.CharField(max_length=255, default='', verbose_name='Название маршрута')
    sights = models.ManyToManyField(Sight, blank=False, verbose_name='Достопримечательности маршрута')

    class Meta:
        verbose_name = 'Маршрут по достопримечательностям'
        verbose_name_plural = 'Маршруты по достопримечательностям'

    def __str__(self):
        return self.title
