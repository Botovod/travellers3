import logging
import os
import psycopg2

from django.core.paginator import Paginator
from django.conf import settings
from django.shortcuts import render
from psycopg2 import OperationalError

from django.views.generic.list import ListView
from laboratory.db_connector import ConnPsql

from geography.models import SightPhoto


class TopCitiesList(ListView):
    template_name = 'laboratory/topcities.html'

    def get(self, request):
        regions = get_data()

        paginator = Paginator(regions, settings.PAGINATION_COUNT_ONE)
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        return render(request,
                      template_name=self.template_name,
                      context={'catalog': contacts})


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
            if photo:
                image = SightPhoto.objects.get(id=photo[0][0])
                if image.file.url.split('.')[-1] not in ("jpg", "JPG", "JPEG", "jpeg"):
                    from travelers.convector_image import convector_to_sight
                    convector_to_sight(image)
                dictionary['photo'] = image
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

            datas = {}                     # {(1, 'Москва - Санкт-Петербург'): [[(1, Moscow), (2, Sbp), ...], Kremle, image_url}
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
                        if img.file.url.split('.')[-1] not in ("jpg", "JPG", "JPEG", "jpeg"):
                            from travelers.convector_image import convector_to_sight
                            convector_to_sight(img)
                        datas[trace].append(img)


        return render(request, self.template_name, {'datas': datas})

#new line


# next line
