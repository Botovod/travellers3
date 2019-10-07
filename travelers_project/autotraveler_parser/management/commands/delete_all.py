from autotraveler_parser.management.commands.delete_cities import Command as cities
from autotraveler_parser.management.commands.delete_regions import Command as regions
from autotraveler_parser.management.commands.delete_sights import Command as sights
from django.core.management.base import BaseCommand

# Clean test's objects
class Command(BaseCommand):

    def handle(self, *args, **kwrags):
        sights()
        cities()
        regions()

        print("All is deleted!!!")
