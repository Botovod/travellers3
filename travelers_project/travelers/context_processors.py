from travelers_project.settings import YMAPS_KEY
from mainpage.models import MainPage

# api v2.1
ymaps_key = "https://api-maps.yandex.ru/2.1/?apikey={}&lang=ru_RU".format(YMAPS_KEY)


def get_vars(request):
    return {'ymaps_key': ymaps_key}


def get_social_urls(request):
    return {'social_urls': MainPage.objects.first()}
