from django.core.management.base import BaseCommand

from geography.models import Sight


def get_coords(original_coords):
    # N056 23.970, E038 44.479
    coords = original_coords.replace(' ', '').replace('.', '').split(',')
    latitude = coords[0][2:4] + '.' + coords[0][4:]
    longitude = coords[1][2:4] + '.' + coords[1][4:]
    return latitude, longitude


def fix_coords():
    sights = Sight.objects.all()
    for sight in sights:
        original_coords = sight.original_coordinates
        if original_coords:
            latitude,  longitude = get_coords(original_coords)
            sight.coordinates = latitude + " " + longitude
            sight.latitude = latitude
            sight.longitude = longitude
            sight.save()


class Command(BaseCommand):
    def handle(self, **options):
        fix_coords()
