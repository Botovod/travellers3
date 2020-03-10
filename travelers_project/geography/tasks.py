import random
from datetime import date

from celery import shared_task
import vk_api

from geography.models import City, Sight
from trips.models import SightTrip, CityTrip
from vk_poster.models import CityPost, SightPost, CityTripPost
from travelers_project.settings import VK_TOKEN, VK_GROUP_ID


class GeographicObject:
    def get_data(self):
        raise NotImplementedError


class CityPostObject(GeographicObject):
    def get_data(self):
        random_item = City.objects.all().order_by('?').first()
        post_settings = CityPost.objects.all().first()

        if post_settings.region:
            region = random_item.get_region
        else:
            region = ''

        if post_settings.hashtags:
            hashtags = random_item.get_hashtags
        else:
            hashtags = ''

        if post_settings.title:
            title = random_item.get_title
        else:
            title = ''

        if post_settings.description:
            description = random_item.get_description
        else:
            description = ''

        if post_settings.image:
            img_path = random_item.get_image_path
        else:
            img_path = ''

        if post_settings.latitude:
            latitude = random_item.get_latitude
        else:
            latitude = ''

        if post_settings.longitude:
            longitude = random_item.get_longitude
        else:
            longitude = ''

        text = title + region + latitude + longitude + description + hashtags

        return img_path, text


class SightPostObject(GeographicObject):
    def get_data(self):
        random_item = Sight.objects.all().order_by('?').first()
        post_settings = SightPost.objects.all().first()

        if post_settings.city:
            city = random_item.get_city
        else:
            city = ''

        if post_settings.title:
            title = random_item.get_title
        else:
            title = ''

        if post_settings.hashtags:
            hashtags = random_item.get_hashtags
        else:
            hashtags = ''

        if post_settings.text:
            description = random_item.get_description
        else:
            description = ''

        if post_settings.image:
            img_path = random_item.get_image_path
        else:
            img_path = ''

        if post_settings.coordinates:
            coordinates = random_item.get_coordinates
        else:
            coordinates = ''

        if post_settings.latitude:
            latitude = random_item.get_latitude
        else:
            latitude = ''

        if post_settings.longitude:
            longitude = random_item.get_longitude
        else:
            longitude = ''

        text = title + city + coordinates + latitude + coordinates + longitude + description + hashtags

        return img_path, text


class TripCityRecentPostObject(GeographicObject):
    def get_data(self):
        random_item = CityTrip.objects.filter(end_date__date__lt=date.today()).order_by('?').first()
        post_settings = CityTripPost.objects.all().first()

        type = 'Тип: завершенное\n'

        if post_settings.title:
            title = random_item.get_title
        else:
            title = ''

        if post_settings.route:
            route = random_item.get_route
        else:
            route = ''

        if post_settings.start_date:
            start_date = random_item.get_start_date
        else:
            start_date = ''

        if post_settings.end_date:
            end_date = random_item.get_end_date
        else:
            end_date = ''

        if post_settings.description:
            description = random_item.get_description
        else:
            description = ''

        text = title + type + route + start_date + end_date + description
        img_path = ''

        return img_path, text


def get_random_object():
    geographic_objects = (
        # CityPostObject(),
        # SightPostObject(),
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
