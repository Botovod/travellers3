from django.db import models


class Traveler(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Trip(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название путешествия')
    start_date = models.DateField(verbose_name='Дата начала путешествия')
    end_date = models.DateField(verbose_name='Дата окончания путешествия')
    description = models.TextField(default='', verbose_name='Описание путешествия')
    traveler = models.ManyToManyField(Traveler, related_name='trip_traveler', verbose_name='Путешественник')

    def __str__(self):
        return self.title
