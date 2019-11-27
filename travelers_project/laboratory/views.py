from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import render

from django.views.generic.list import ListView
from laboratory.db_connector import ConnPsql

from geography.models import SightPhoto
from travelers.convector_image import GetNormalImage


def convert_image(image):
    if image.file.url.split('.')[-1] not in ("jpg", "JPG", "JPEG", "jpeg"):
        GetNormalImage(image).get_image()


def add_item(dictionary, item, value):
    if value:
        if item == 'photo':
            value = SightPhoto.objects.get(id=value)
            convert_image(value)
        dictionary[item] = value
    else:
        dictionary[item] = ''


class TopCitiesList(ListView):
    template_name = 'laboratory/topcities.html'

    def get(self, request):
        with ConnPsql() as conn:
            cursor = conn.cursor()
            cursor.execute(
                '''
                WITH
                regions as 
                (SELECT id, title 
                FROM geography_region
                ORDER BY id),
                cities as
                (SELECT city.region_id, city.id, city.title
                FROM geography_city city
                WHERE rating = (SELECT MAX(rating) FROM geography_city where region_id = city.region_id)
                GROUP BY city.region_id, city.id),
                sights as
                (SELECT sight.city_id, sight.id, sight.title
                FROM geography_sight sight
                WHERE rating = (SELECT MAX(rating) FROM geography_sight where city_id = sight.city_id)
                GROUP BY sight.city_id, sight.id),
                photos as
                (SELECT photo.sight_id, photo.id, photo.file
                FROM geography_sightphoto photo
                WHERE rating = (SELECT MAX(rating) FROM geography_sightphoto WHERE sight_id = photo.sight_id)
                GROUP BY photo.sight_id, photo.id)
                SELECT 
                regions.id, regions.title,
                cities.id, cities.title,
                sights.id, sights.title,
                photos.id, photos.file
                FROM regions
                LEFT JOIN cities
                ON regions.id = cities.region_id
                LEFT JOIN sights
                ON cities.id = sights.city_id
                LEFT JOIN photos
                ON sights.id = photos.sight_id;
                '''
            )
            data = cursor.fetchall()
            context = []
            for x in data:
                dictionary = dict()
                add_item(dictionary, 'region', x[1])
                add_item(dictionary, 'city', x[3])
                add_item(dictionary, 'sight', x[5])
                add_item(dictionary, 'photo', x[6])
                context.append(dictionary)

            paginator = Paginator(context, settings.PAGINATION_COUNT_ONE)
            page = request.GET.get('page')
            contacts = paginator.get_page(page)
        return render(request, template_name=self.template_name, context={'catalog': contacts})


class TopTracesListView(ListView):
    template_name = 'laboratory/toptraces.html'

    def get(self, request):
        with ConnPsql() as conn:
            cursor = conn.cursor()
            # traces
            cursor.execute(
                '''
                    SELECT id, title FROM traces_routebycities;
                '''
            )
            traces = cursor.fetchall()  # [(1, 'Москва - Санкт-Петербург')]

            datas = {}  # {(1, 'Москва - Санкт-Петербург'): [[(1, Moscow), (2, Sbp), ...], Kremle, image_url}
            for trace in traces:
                # cities
                cursor.execute(
                    f'''
                        SELECT geography_city.id, title
                        FROM geography_city
                        INNER JOIN traces_citiesrelationship
                        ON (geography_city.id = traces_citiesrelationship.city_id)
                        WHERE traces_citiesrelationship.route_id = {trace[0]};
                    '''
                )
                cities = cursor.fetchall()

                # popoular sight
                cursor.execute(
                    f'''
                        SELECT id, title, rating
                        FROM geography_sight
                        WHERE city_id IN {tuple(id[0] for id in cities)}
                        AND rating = (SELECT MAX(rating) FROM geography_sight
                        WHERE city_id IN {tuple(id[0] for id in cities)})
                        LIMIT 1
                    '''
                )
                sight = cursor.fetchall()
                datas[trace] = [cities, sight]

                # popular image
                if sight:
                    cursor.execute(
                        f'''
                            SELECT id
                            FROM geography_sightphoto
                            WHERE sight_id = {sight[0][0]}
                            AND rating = (SELECT MAX(rating) FROM geography_sightphoto
                            WHERE sight_id = {sight[0][0]})
                            LIMIT 1
                        '''
                    )
                    image = cursor.fetchall()
                    if image:
                        img = SightPhoto.objects.only('file').get(id=image[0][0])

                        datas[trace].append(img)
        return render(request, self.template_name, {'datas': datas})
