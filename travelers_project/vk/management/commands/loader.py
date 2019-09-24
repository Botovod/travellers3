import asyncio

from django.core.management.base import BaseCommand

from vk.management.commands.photos import main as m1
from vk.management.commands.saver import main as m2


async def main():
    await m1()
    await m2()


class Command(BaseCommand):
    def handle(self, **options):
        asyncio.run(main())
