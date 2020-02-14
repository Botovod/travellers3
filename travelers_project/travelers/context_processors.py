from travelers_project.settings import YMAPS_KEY
from mainpage.models import MainPage
from trips.models import Traveler, CityTrip, SightTrip
from datetime import date


# api v2.1
ymaps_key = "https://api-maps.yandex.ru/2.1/?apikey={}&lang=ru_RU".format(YMAPS_KEY)


def get_vars(request):
    return {'ymaps_key': ymaps_key}


def get_social_urls(request):
    return {'social_urls': MainPage.objects.first()}


def get_num_of_completed_trips(request):
    num_of_city_trips = CityTrip.objects.filter(end_date__date__lt=date.today()).count()
    return {'num_of_completed_trips': num_of_city_trips}


def get_num_of_travelers(request):
    return {'num_of_travelers': Traveler.objects.count()}
