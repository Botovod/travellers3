import aiohttp
import asyncio
import json
import os

from vk.management.commands.photos import filename

image_folder = 'images'
curDirectory = os.path.dirname(os.path.abspath(__file__))
dirMainName = os.path.join(curDirectory, image_folder)


async def download_photo(info, session):
    async with session.get(info['url']) as response:
        data = await response.read()
        write_image(data, info)


def write_image(data, info):
    if not os.path.exists(dirMainName):
        os.mkdir(dirMainName)

    dir1 = os.path.join(dirMainName, info['album'])
    if not os.path.exists(dir1):
        os.mkdir(dir1)

    dir2 = os.path.join(dir1, str(info['owner_id']))
    if not os.path.exists(dir2):
        os.mkdir(dir2)

    dir3 = os.path.join(dir2, str(info['album_id']))
    if not os.path.exists(dir3):
        os.mkdir(dir3)

    picture = info['url'].split('/')[-1]
    file_path = os.path.join(dir3, picture)

    with open(file_path, 'wb') as file:
        file.write(data)


async def main():
    tasks = []
    data = json.load(open(filename))
    async with aiohttp.ClientSession() as session:
        for i in data:
            task = asyncio.create_task(download_photo(i, session))
            tasks.append(task)
        await asyncio.gather(*tasks)
