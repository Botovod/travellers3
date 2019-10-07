import os
import asyncio
import logging
from time import time
from django.core.management.base import BaseCommand
from autotraveler_parser.regions import main as regions
from autotraveler_parser.cities import main as cities
from autotraveler_parser.sights import main as sights

path_to_log = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "info.log")
logging.basicConfig(filename=path_to_log, filemode='w', level=logging.INFO)

async def main():
    start = time()

    print("Add regions..........\n")
    await regions()
    print()

    print("Add cities..........\n")
    await cities()
    print()

    print("Add sights..........\n")
    await sights()
    print()

    print("Done....!!!")
    total_time = time() - start
    logging.info(f"{total_time}")


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        asyncio.run(main())
