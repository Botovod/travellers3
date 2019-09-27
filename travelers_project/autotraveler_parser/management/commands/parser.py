import asyncio
from django.core.management.base import BaseCommand
from autotraveler_parser.regions import region, regions
from autotraveler_parser.cities import town, towns


async def main():
    semaphore = asyncio.Semaphore(20)

    links_regions = await regions(semaphore)
    links_towns = await towns(semaphore)

    tasks = []

    for link in links_regions:
        task = asyncio.create_task(region(link, semaphore))
        tasks.append(task)

    for link in links_towns:
        task = asyncio.create_task(town(link, semaphore))
        tasks.append(task)

    await asyncio.gather(*tasks)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        asyncio.run(main())
