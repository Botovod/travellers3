import logging
import psycopg2

from django.conf import settings
from django.shortcuts import render
from psycopg2 import OperationalError

from sorl.thumbnail import get_thumbnail

from django.views.generic.list import ListView
from laboratory.db_connector import ConnPsql


class TopCitiesList(ListView):
    template_name = 'laboratory/topcities.html'
    paginate_by = 10

    def get(self, request):
        regions = get_data()

        return render(request, template_name=self.template_name, context={'regions': regions})


def get_data():
    data = []
    try:
        conn = psycopg2.connect(dbname=settings.DATABASES['default']['NAME'],
                                user=settings.DATABASES['default']['USER'],
                                host=settings.DATABASES['default']['HOST'],
                                password=settings.DATABASES['default']['PASSWORD'])
    except (OperationalError, KeyError):
        logging.exception('Unable to open DB')
    else:
        cur = conn.cursor()
        cur.execute('''SELECT id, title
                       FROM geography_region;''')
        regions = cur.fetchall()
        for region_id, title in regions:
            dictionary = dict()
            dictionary['region'] = title
            cur.execute('''SELECT id, title
                           FROM geography_city
                           WHERE region_id = {}
                           AND rating =
                           (SELECT max(rating)
                           FROM geography_city
                           WHERE region_id = {}) ;'''.format(region_id, region_id))
            city = cur.fetchall()
            try:
                dictionary['city'] = city[0][1]
            except IndexError:
                dictionary['city'] = ''
            cur.execute('''SELECT sight.id, sight.title
                           FROM geography_city city
                           LEFT JOIN geography_sight sight
                           ON city.id = sight.city_id
                           WHERE city.region_id = {}
                           AND sight.rating =
                           (SELECT max(sight.rating)
                           FROM geography_city city
                           LEFT JOIN geography_sight sight
                           ON city.id = sight.city_id
                           WHERE city.region_id = {}) ;'''.format(region_id, region_id))
            sight = cur.fetchall()
            try:
                dictionary['sight'] = sight[0][1]
            except IndexError:
                dictionary['sight'] = ''

            cur.execute('''SELECT photo.id, photo.file
                           FROM geography_sight sight
                           LEFT JOIN geography_sightphoto photo
                           ON photo.sight_id = sight.id
                           WHERE sight.city_id
                           IN (SELECT city.id
                           FROM geography_city city
                           WHERE city.region_id={})
                           AND photo.rating =
                           (SELECT max(photo.rating)
                           FROM geography_sight sight
                           LEFT JOIN geography_sightphoto photo
                           ON photo.sight_id = sight.id
                           WHERE sight.city_id
                           IN (SELECT city.id
                           FROM geography_city city
                           WHERE city.region_id={}));'''.format(region_id, region_id))
            photo = cur.fetchall()
            try:
                im = get_thumbnail(photo[0][1], '100x100', crop='center', quality=99)
                dictionary['photo'] = im.url
            except IndexError:
                dictionary['photo'] = ''

            data.append(dictionary)
        conn.commit()
        cur.close()
        conn.close()
    return data


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
            traces = cursor.fetchall()      # [(1, 'Москва - Санкт-Петербург')]

            routes = {}                     # {(1, 'Москва - Санкт-Петербург'): [[(1, Moscow), (2, Sbp), ...], Kremle, image_url}
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
                        WHERE city_id IN {tuple(i[0] for i in cities)}
                        AND rating = (SELECT MAX(rating) FROM geography_sight
                        WHERE city_id IN {tuple(i[0] for i in cities)})
                        LIMIT 1
                    '''
                )
                sights = cursor.fetchall()

                routes[trace] = [cities, sights]

        return render(request, self.template_name, {'routes': routes})
