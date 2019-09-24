import asyncio
import aiohttp

from django.core.management.base import BaseCommand
from travelers_project.settings import VK_TOKEN
from travelers_project.settings import VK_API_VERSION

# from django.conf.settings import VK_TOKEN
# from django.conf.settings import VK_API_VERSION

# from travelers_project.travelers_project.settings import
# from travelers_project.travelers_project.settings import VK_API_VERSION

messages = [
    ('1', 'photo562731269_457239032',),
    ('2', 'photo562731269_457239030'),
    ('3', 'photo562731269_457239027'),
    ('4', 'photo562731269_457239025'),
    ('5', 'photo562731269_457239023'),
    ('6', 'photo562731269_457239024'),

]


async def create_post(session, message, attachment):
    await session.get('https://api.vk.com/method/wall.post',
                      params={
                          'owner_id': -186823704,
                          'message': message,
                          'attachments': attachment,
                          'access_token': VK_TOKEN,
                          'v': VK_API_VERSION,
                      })


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for message in messages:
            tasks.append(asyncio.create_task(create_post(session, message[0], message[1])))
        await asyncio.gather(*tasks)


class Command(BaseCommand):
    def handle(self, **options):
        asyncio.run(main())
