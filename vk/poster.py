import asyncio
import aiohttp

from travelers_project.travelers_project.settings import VK_TOKEN
from travelers_project.travelers_project.settings import VK_API_VERSION

messages = [
    ('first post', 'photo562731269_457239020',),
    ('second_post', 'photo562731269_457239019'),
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


if __name__ == '__main__':
    asyncio.run(main())
