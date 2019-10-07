import asyncio
import aiohttp
import datetime
import time
from urllib.request import urlopen
from django.core.management.base import BaseCommand
from django.core.files.temp import NamedTemporaryFile

import vk
from vk.exceptions import VkAPIError

from travelers_project.settings import VK_APP_ID, VK_LOGIN, VK_PASSWORD, VK_API_VERSION

from vkapp.models import Album, Photo

owner_id = 2406559
photos = []
photos_for_load = []


def get_vk_api():
    session = vk.AuthSession(app_id=VK_APP_ID,
                             user_login=VK_LOGIN,
                             user_password=VK_PASSWORD,
                             scope='photos')
    vkapi = vk.API(session,
                   v=VK_API_VERSION,
                   lang='ru',
                   timeout=1000)
    return vkapi


def get_albums(vkapi):
    albums = vkapi.photos.getAlbums(owner_id=owner_id,
                                    extended=1,
                                    need_system=0)
    return albums


async def get_or_create_album(album, session):
    async with session:
        new_album, created = Album.objects.update_or_create(vk_id=album['id'],
                                                            owner_id=album['owner_id'])
        new_album.title = album['title'],
        new_album.description = album['description'],
        new_album.created = datetime.datetime.fromtimestamp(int(album['created']))
        new_album.updated = datetime.datetime.fromtimestamp(int(album['updated']))
        new_album.save()

    return new_album


def get_album_photos(vkapi, album):
    while True:
        try:
            new_photos = vkapi.photos.get(owner_id=album.owner_id,
                                          album_id=str(album.vk_id),
                                          count=1000,
                                          extended=1)
        except VkAPIError as e:
            time.sleep(1)
        else:
            break
    return new_photos['items']


async def get_photo(photo, session):
    async with session:
        new_photo, created = Photo.objects.update_or_create(vk_id=photo['id'],
                                                            album_id=photo['album_id'],
                                                            owner_id=photo['owner_id'])
        url = get_photo_url(photo['sizes'])
        new_photo.url = url
        new_photo.date = datetime.datetime.fromtimestamp(int(photo['date']))
        new_photo.save()
        if created:
            photos_for_load.append(photo)


def get_photo_url(*photo_urls):
    url = ''
    try:
        n = 0
        max_quality = max(photo_urls[0][n]['width'], photo_urls[0][n]['height'])
        for i in range(1, len(photo_urls[0])):
            size = max(photo_urls[0][i]['width'], photo_urls[0][i]['height'])
            if size > max_quality:
                n = i
                max_quality = size
        if max_quality > 0:
            url = photo_urls[0][n]['url']
    except KeyError:
        return ''
    return url


async def load_photo(photo, session):
    async with session:
        url = photo.url
        if url != '':
            filename = url.split('/')[-1]
            img_temp = NamedTemporaryFile()
            img_temp.write(urlopen(url).read())
            photo.image.save(filename, img_temp, save=False)
            print('Image {} is saving now'.format(filename))
            img_temp.flush()


async def vkloader():
    vkapi = get_vk_api()
    albums = get_albums(vkapi)
    album_tasks = []
    photo_tasks = []
    # create albums & get album_photos
    async with aiohttp.ClientSession() as session:
        for album in albums['items']:
            album_tasks.append(asyncio.create_task(get_or_create_album(album, session)))
        await asyncio.gather(*album_tasks)

        for album in Album.objects.all():
            photos.extend(get_album_photos(vkapi, album))

        # get photos
        for photo in photos:
            photo_tasks.append(asyncio.create_task(get_photo(photo, session)))
        await asyncio.gather(*photo_tasks)

        # get photos
        for photo in photos_for_load:
            photo_tasks.append(asyncio.create_task(load_photo(photo)))
        await asyncio.gather(*photo_tasks)

        for photo in Photo.objects.all():
            photo_tasks.append(asyncio.create_task(load_photo(photo, session)))
        await asyncio.gather(*photo_tasks)


class Command(BaseCommand):
    def handle(self, **options):
        asyncio.run(vkloader())
