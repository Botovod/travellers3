import json
import os
from django.conf import settings

from django.core.management.base import BaseCommand

from geography.models import City, Sight


def get_coords(original_coords):
    # N056 23.970, E038 44.479
    coords = original_coords.replace(' ', '').replace('.', '').split(',')
    latitude = coords[0][2:4] + '.' + coords[0][4:]
    longitude = coords[1][2:4] + '.' + coords[1][4:]
    return latitude, longitude


def fix_sight_coords():
    sights = Sight.objects.all()
    for sight in sights:
        original_coords = sight.original_coordinates
        if original_coords:
            latitude, longitude = get_coords(original_coords)
            sight.coordinates = latitude + " " + longitude
            sight.latitude = latitude
            sight.longitude = longitude
            sight.save()


def fix_city_coords():
    cities = City.objects.all()
    for city in cities:
        original_coords = city.centre_coordinates
        if original_coords:
            latitude, longitude = get_coords(original_coords)
            city.centre_coordinates = f'{latitude} {longitude}'
            city.latitude = latitude
            city.longitude = longitude
        else:
            try:
                sight = city.sight.all()[0]
            except IndexError:
                pass
            else:
                city.centre_coordinates = sight.coordinates
                city.latitude = sight.latitude
                city.longitude = sight.longitude
        city.save()


def get_data_from_file():
    filename = os.path.join(settings.BASE_DIR, 'static', 'json', 'cities.json')
    with open(filename, 'r') as file:
        data = json.load(file)
        cities = City.objects.all()
        for city in cities:
            if city.title in data.keys():
                city.centre_coordinates = f'{data[city.title][0]} {data[city.title][1]}'
                city.latitude = data[city.title][0]
                city.longitude = data[city.title][1]
                city.save()


class Command(BaseCommand):
    def handle(self, **options):
        get_data_from_file()
        fix_sight_coords()
        fix_city_coords()
