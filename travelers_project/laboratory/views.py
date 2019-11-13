import logging
import psycopg2

from django.conf import settings
from django.shortcuts import render
from psycopg2 import OperationalError

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
                           (SELECT Max(rating)
                           FROM geography_city
                           WHERE region_id = {}) ;'''.format(region_id, region_id))
            city = cur.fetchall()
            try:
                dictionary['city'] = city[0][1]
            except IndexError:
                dictionary['city'] = ''
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

            cursor.execute(
                '''
                    SELECT id, title FROM traces_routebycities;
                '''
            )
            traces = cursor.fetchall()      # [(1, 'Москва - Санкт-Петербург')]

            routes = {}                     # {(1, 'Москва - Санкт-Петербург'): [[(1, Moscow), (2, Sbp), ...], Kremle, image_url}
            for trace in traces:
                cursor.execute(
                    f'''
                        SELECT geography_city.id, title
                        FROM geography_city
                        INNER JOIN traces_citiesrelationship
                        ON (geography_city.id = traces_citiesrelationship.city_id)
                        WHERE traces_citiesrelationship.route_id = {trace[0]}
                    '''
                )
                cities = cursor.fetchall()
                routes[trace] = cities

        return render(request, self.template_name, {'routes': routes})
