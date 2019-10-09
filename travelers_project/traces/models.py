from django.db import models

from geography.models import City
from geography.models import Sight


class RouteByCities(models.Model):
    title = models.CharField(max_length=255, default='', verbose_name='Название маршрута')
    cities = models.ManyToManyField(City, through='CitiesRelationship')
    description = models.TextField(default="")

    class Meta:
        verbose_name = 'Маршрут по городам'
        verbose_name_plural = 'Маршруты по городам'

    def __str__(self):
        return self.title


class CitiesRelationship(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    route = models.ForeignKey(RouteByCities, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    class Meta:
        unique_together = [['route', 'position']]

    def __str__(self):
        return '{}-{}'.format(self.route.title, self.city.title)


class RouteBySights(models.Model):
    title = models.CharField(max_length=255, default='', verbose_name='Название маршрута')
    sights = models.ManyToManyField(Sight,
                                    through='SightsRelationship',
                                    verbose_name='Достопримечательности маршрута')
    description = models.TextField(default="")

    class Meta:
        verbose_name = 'Маршрут по достопримечательностям'
        verbose_name_plural = 'Маршруты по достопримечательностям'

    def __str__(self):
        return self.title


class SightsRelationship(models.Model):
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE)
    route = models.ForeignKey(RouteBySights, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    class Meta:
        unique_together = [['route', 'position']]

    def __str__(self):
        return '{}-{}'.format(self.route.title, self.sight.title)
