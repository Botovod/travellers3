from geography.models import City, Region, Sight
from django.core.management.base import BaseCommand

# Clean test's objects
class Command(BaseCommand):

    def handle(self, *args, **kwrags):
        Region.objects.all().delete()
        Sight.objects.all().delete()
        City.objects.all().delete()

        print("All is deleted!!!")
