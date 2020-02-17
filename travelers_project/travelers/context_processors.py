from travelers_project.settings import YMAPS_KEY
from mainpage.models import SocialMedia
from trips.models import Traveler, CityTrip
from datetime import date


# api v2.1
ymaps_key = "https://api-maps.yandex.ru/2.1/?apikey={}&lang=ru_RU".format(YMAPS_KEY)


def get_vars(request):
    return {'ymaps_key': ymaps_key}


def get_facebook_url(request):
    return {'facebook_url': SocialMedia.objects.get(title="Facebook")}


def get_vk_url(request):
    return {'vk_url': SocialMedia.objects.get(title="Vkontakte")}


def get_instagram_url(request):
    return {'instagram_url': SocialMedia.objects.get(title="Instagram")}


def get_num_of_completed_trips(request):
    num_of_city_trips = CityTrip.objects.filter(end_date__date__lt=date.today()).count()
    return {'num_of_completed_trips': num_of_city_trips}


def get_num_of_travelers(request):
    return {'num_of_travelers': Traveler.objects.count()}
