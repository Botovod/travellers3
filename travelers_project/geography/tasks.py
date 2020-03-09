from __future__ import absolute_import, unicode_literals
import os
import random
from datetime import date

from celery import shared_task
import vk_api

from geography.models import City, Sight
from trips.models import SightTrip, CityTrip
from vk_poster.models import CityPost, SightPost, CityTripPost
from travelers_project.settings import MEDIA_ROOT, BASE_DIR, VK_TOKEN, VK_GROUP_ID


class GeographicObject:
    def get_data(self):
        raise NotImplementedError


class CityPostObject(GeographicObject):
    def get_data(self):
        random_item = City.objects.all().order_by('?')[:1].get()
        post_settings = CityPost.objects.filter()[:1].get()

        if post_settings.region:
            if random_item.region:
                region = f'Регион: {random_item.region}\n'
            else:
                region = ''
        else:
            region = ''

        if post_settings.title:
            if random_item.title:
                title = f'{random_item.title}\n'
            else:
                title = ''
        else:
            title = ''

        if post_settings.description:
            if random_item.description:
                description = f'\n{random_item.description}'
            else:
                description = ''
        else:
            description = ''

        if post_settings.image:
            if random_item.image:
                img_path = os.path.join(MEDIA_ROOT, str(random_item.image))
            else:
                img_path = os.path.join(BASE_DIR, 'static/images/not-foto.png')
        else:
            img_path = ''

        if post_settings.latitude:
            if random_item.latitude:
                latitude = f'Широта: {random_item.latitude}\n'
            else:
                latitude = ''
        else:
            latitude = ''

        if post_settings.longitude:
            if random_item.longitude:
                longitude = f'Долгота: {random_item.longitude}\n'
            else:
                longitude = ''
        else:
            longitude = ''

        text = title + region + latitude + longitude + description

        return img_path, text


class SightPostObject(GeographicObject):
    def get_data(self):
        random_item = Sight.objects.all().order_by('?')[:1].get()
        post_settings = SightPost.objects.filter()[:1].get()

        if post_settings.city:
            if random_item.city:
                city = f'Город: {random_item.city}\n'
            else:
                city = ''
        else:
            city = ''

        if post_settings.title:
            if random_item.title:
                title = f'{random_item.title}\n'
            else:
                title = ''
        else:
            title = ''

        if post_settings.text:
            if random_item.text:
                description = f'\n{random_item.text}'
            else:
                description = ''
        else:
            description = ''

        if post_settings.image:
            if random_item.image:
                img_path = os.path.join(MEDIA_ROOT, str(random_item.image))
            else:
                img_path = os.path.join(BASE_DIR, 'static/images/not-foto.png')
        else:
            img_path = ''

        if post_settings.coordinates:
            if random_item.coordinates:
                coordinates = f'Координаты: {random_item.coordinates}\n'
            else:
                coordinates = ''
        else:
            coordinates = ''

        if post_settings.latitude:
            if random_item.latitude:
                latitude = f'Широта: {random_item.latitude}\n'
            else:
                latitude = ''
        else:
            latitude = ''

        if post_settings.longitude:
            if random_item.longitude:
                longitude = f'Долгота: {random_item.longitude}\n'
            else:
                longitude = ''
        else:
            longitude = ''

        text = title + city + coordinates + latitude + longitude + description

        return img_path, text


class TripCityRecentPostObject(GeographicObject):
    def get_data(self):
        random_item = CityTrip.objects.filter(end_date__date__lt=date.today()).order_by('?')[:1].get()
        post_settings = CityTripPost.objects.filter()[:1].get()

        type = 'Тип: завершенное\n'

        if post_settings.title:
            if random_item.title:
                title = f'{random_item.title}\n'
            else:
                title = ''
        else:
            title = ''

        if post_settings.route:
            if random_item.route:
                route = f'Маршрут: {random_item.route}\n'
            else:
                route = ''
        else:
            route = ''

        if post_settings.start_date:
            if random_item.start_date:
                start_date = f'Дата начала: {random_item.start_date.strftime("%d/%m/%Y")}\n'
            else:
                start_date = ''
        else:
            start_date = ''

        if post_settings.end_date:
            if random_item.end_date:
                end_date = f'Дата окончания: {random_item.end_date.strftime("%d/%m/%Y")}\n'
            else:
                end_date = ''
        else:
            end_date = ''

        if post_settings.description:
            if random_item.description:
                description = f'\n{random_item.description}'
            else:
                description = ''
        else:
            description = ''

        text = title + type + route + start_date + end_date + description
        img_path = ''

        return img_path, text


def get_random_object():
    geographic_objects = (
        CityPostObject(),
        SightPostObject(),
        TripCityRecentPostObject(),
    )

    geographic_object = random.choice(geographic_objects)

    return geographic_object.get_data()


def get_session():
    vk_session = vk_api.VkApi(token=VK_TOKEN)

    return vk_session


def upload_photo():
    vk_session = get_session()
    path, text = get_random_object()
    if path:
        upload = vk_api.VkUpload(vk_session)
        photo = upload.photo_wall(
            photos=path,
            group_id=VK_GROUP_ID)

        photo_url = 'photo{}_{}'.format(photo[0]['owner_id'], photo[0]['id'])
    else:
        photo_url = ''
    return photo_url, text


def create_wall_post(post):
    vk_session = get_session()
    vk = vk_session.get_api()

    attachments = post[0]
    if attachments:
        vk.wall.post(
            owner_id='-' + str(VK_GROUP_ID),
            message=post[1],
            from_group=True,
            attachments=post[0])
    else:
        vk.wall.post(
            owner_id='-' + str(VK_GROUP_ID),
            message=post[1],
            from_group=True)


@shared_task
def post():
    create_wall_post(upload_photo())
