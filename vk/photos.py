import asyncio
import aiohttp
import json

from time import time

from travelers_project.travelers_project.settings import VK_TOKEN
from travelers_project.travelers_project.settings import VK_API_VERSION

queries = ['Достопримечательность']
photos = []
filename = 'album.json'

COUNT = 100


async def get_response(q, offset, session):
    async with session.get('https://api.vk.com/method/photos.search',
                           params={
                               'q': q,
                               'access_token': VK_TOKEN,
                               'v': VK_API_VERSION,
                               'offset': offset,
                               'count': COUNT,
                           }) as response:
        data = await response.json()
    return data


async def get_photos(data, q):
    new_photos = []
    try:
        for photo in data['response']['items']:
            sizes = photo['sizes']
            n = 0
            max_quality = max(sizes[n]['width'], sizes[n]['height'])
            for i in range(1, len(sizes)):
                size = max(sizes[i]['width'], sizes[i]['height'])
                if size > max_quality:
                    n = i
                    max_quality = size
            if max_quality > 0:
                max_size_url = sizes[n]['url']
                new_photos.append({'album': q,
                                   'owner_id': abs(photo['album_id']),
                                   'album_id': abs(photo['owner_id']),
                                   'url': max_size_url})
    except KeyError:
        print('No such key')
    else:
        photos.extend(new_photos)


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for query in queries:
            offset = 0
            data = await get_response(query, offset, session)
            size = data['response']['count']
            asyncio.create_task(get_photos(data, query))
            while offset <= size:
                offset += COUNT
                task1 = asyncio.create_task(get_response(query, offset, session))
                tasks.append(task1)
                task2 = asyncio.create_task(get_photos(data, query))
                tasks.append(task2)
        await asyncio.gather(*tasks)


def write_json(data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    start = time()
    asyncio.run(main())

    write_json(photos)
    print(time() - start)
