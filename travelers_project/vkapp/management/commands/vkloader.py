import datetime
from urllib.request import urlopen
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

import vk

from travelers_project.settings import VK_APP_ID, VK_LOGIN, VK_PASSWORD, VK_API_VERSION

from vkapp.models import Album, Photo

owner_id = 2406559


class Command(BaseCommand):
    def get_photo_url(self, *urls):
        max_size_url = ''
        try:
            n = 0
            max_quality = max(urls[0][n]['width'], urls[0][n]['height'])
            for i in range(1, len(urls[0])):
                size = max(urls[0][i]['width'], urls[0][i]['height'])
                if size > max_quality:
                    n = i
                    max_quality = size
            if max_quality > 0:
                max_size_url = urls[0][n]['url']
        except KeyError:
            return ''
        return max_size_url

    def handle(self, **options):
        session = vk.AuthSession(app_id=VK_APP_ID,
                                 user_login=VK_LOGIN,
                                 user_password=VK_PASSWORD,
                                 scope='photos')
        vkapi = vk.API(session,
                       v=VK_API_VERSION,
                       lang='ru',
                       timeout=1000)

        albums = vkapi.photos.getAlbums(owner_id=owner_id,
                                        extended=1,
                                        need_system=0)

        for album in albums['items']:
            new_album = Album(vk_id=album['id'],
                              owner_id=album['owner_id'],
                              title=album['title'],
                              description=album['description'],
                              created=datetime.datetime.fromtimestamp(int(album['created'])),
                              updated=datetime.datetime.fromtimestamp(int(album['updated'])))
            try:
                new_album.save()
            except IntegrityError:
                pass

            photos = vkapi.photos.get(owner_id=owner_id,
                                      album_id=album['id'],
                                      count=1000,
                                      extended=1)
            for photo in photos['items']:
                new_photo = Photo(vk_id=photo['id'],
                                  album_id=photo['album_id'],
                                  owner_id=photo['owner_id'])
                try:
                    new_photo.save()
                except IntegrityError:
                    continue
                else:
                    sizes = photo['sizes']
                    url = self.get_photo_url(sizes)
                    if url != '':
                        new_photo.url = url
                        filename = url.split('/')[-1]
                        img_temp = NamedTemporaryFile()
                        img_temp.write(urlopen(url).read())
                        new_photo.image.save(filename, img_temp, save=False)
                        new_photo.date = datetime.datetime.fromtimestamp(int(photo['date']))
