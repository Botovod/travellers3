from __future__ import absolute_import, unicode_literals
from celery import shared_task
import vk_api

from geography.models import City, Sight
from trips.models import SightTrip, CityTrip
from travelers_project.settings import MEDIA_ROOT, BASE_DIR, VK_TOKEN, VK_GROUP_ID
import os
import random
from datetime import date



class GeographicObject:
    def get_data(self):
        raise NotImplementedError


class CityPost(GeographicObject):
    def get_data(self):
        cities = City.objects.all()
        random_item = random.choice(cities)

        if random_item.description:
            text = f'{random_item.title}\nРегион: {random_item.region}\n\n{random_item.description}'
        else:
            text = f'{random_item.title}\nРегион: {random_item.region}'
        if random_item.image:
            img_path = os.path.join(MEDIA_ROOT, str(random_item.image))
        else:
            img_path = os.path.join(BASE_DIR, 'static/images/not-foto.png')
        return img_path, text


class SightPost(GeographicObject):
    def get_data(self):
        sights = Sight.objects.all()
        random_item = random.choice(sights)

        if random_item.text:
            text = f'{random_item.title}\nГород: {random_item.city}\n\n{random_item.text}'
        else:
            text = f'{random_item.title}\nГород: {random_item.city}'

        if random_item.image:
            img_path = os.path.join(MEDIA_ROOT, str(random_item.image))
        else:
            img_path = os.path.join(BASE_DIR, 'static/images/not-foto.png')

        return img_path, text


class TripCityRecentPost(GeographicObject):
    def get_data(self):
        trips = CityTrip.objects.filter(end_date__date__lt=date.today())
        random_item = random.choice(trips)

        text = (
            f'Название путешествия: {random_item.title}\n\n'
            f'Тип: завершенное\n'
            f'Маршрут: {random_item.route}\n'
            f'Дата: {random_item.start_date.strftime("%d/%m/%Y")}-{random_item.end_date.strftime("%d/%m/%Y")}'
            f'\n\n{random_item.description}'
        )

        img_path = os.path.join(BASE_DIR, 'static/images/not-foto.png')

        return img_path, text


class TripCityFuturePost(GeographicObject):
    def get_data(self):
        print('furute trip')


class TripSightRecentPost(GeographicObject):
    def get_data(self):
        print('furute trip')


class TripSightFuturePost(GeographicObject):
    def get_data(self):
        print('furute trip')


def get_random_object():
    geographic_objects = (
        CityPost(),
        SightPost(),
        TripCityRecentPost(),
        # TripCityFuturePost(),
        # TripSightRecentPost(),
        # TripSightFuturePost(),
    )

    geographic_object = random.choice(geographic_objects)

    return geographic_object.get_data()


def get_session():
    vk_session = vk_api.VkApi(token=VK_TOKEN)

    return vk_session


def upload_photo():
    vk_session = get_session()
    path, text = get_random_object()

    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_wall(
        photos=path,
        group_id=VK_GROUP_ID)

    photo_url = 'photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])

    return photo_url, text


def create_wall_post(post):
    vk_session = get_session()

    vk = vk_session.get_api()

    vk.wall.post(
        owner_id='-' + str(VK_GROUP_ID),
        message=post[1],
        from_group=True,
        attachments=post[0])


@shared_task
def post():
    create_wall_post(upload_photo())
