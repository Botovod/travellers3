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
                WITH t as (
                SELECT region.id as region_id, region.title as region,
                city.id as city_id, city.title as city, city.rating as city_rating,
                sight.id as sight_id, sight.title as sight, sight.rating as sight_rating,
                photo.id as photo_id, photo.rating as photo_rating
                
                FROM geography_region region
                LEFT JOIN geography_city city
                ON region.id = city.region_id
                LEFT JOIN geography_sight sight
                ON sight.city_id = city.id
                LEFT JOIN geography_sightphoto photo
                ON photo.sight_id = sight.id
                ),
                
                city_table as (
                SELECT region_id, MIN(city) as city
                FROM t
                WHERE city_rating IN (SELECT max(city_rating) FROM t WHERE t.region_id = region_id GROUP BY region)
                GROUP BY region_id
                ORDER BY region_id
                ),
                
                sight_table as (
                SELECT region_id, MIN(sight) as sight
                FROM t
                WHERE sight_rating IN (SELECT max(sight_rating) FROM t WHERE t.region_id = region_id GROUP BY region_id)
                GROUP BY region_id
                ORDER BY region_id
                ),
                
                photo_table as (
                SELECT region_id, MIN(photo_id) as photo_id
                FROM t
                WHERE photo_rating IN (SELECT max(photo_rating) FROM t WHERE t.region_id = region_id GROUP BY region)
                GROUP BY region_id
                ORDER BY region_id
                )
                
                SELECT region.title, city.city, sight.sight, photo.photo_id
                FROM geography_region region
                LEFT JOIN city_table city
                ON region.id = city.region_id
                JOIN sight_table sight
                ON city.region_id = sight.region_id
                JOIN photo_table photo
                ON sight.region_id = photo.region_id;
                '''
            )
            data = cursor.fetchall()
            context = []
            for x in data:
                dictionary = dict()
                add_item(dictionary, 'region', x[0])
                add_item(dictionary, 'city', x[1])
                add_item(dictionary, 'sight', x[2])
                add_item(dictionary, 'photo', x[3])
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
            cursor.execute(
                '''
                    WITH t as(
                    SELECT tr.route_id as route, 
                    sight.id as sight_id, sight.title as sight, sight.rating as sight_rating,
                    city.id as city_id, city.title as city, city.rating as city_rating,
                    ph.id as photo_id,  ph.rating as photo_rating
                    
                    FROM traces_citiesrelationship tr
                    LEFT JOIN geography_city city
                    ON tr.city_id = city.id
                    LEFT JOIN geography_sight sight
                    ON sight.city_id = city.id
                    LEFT JOIN geography_sightphoto ph
                    ON ph.sight_id = sight.id
                    ORDER BY tr.route_id
                    ),
                    
                    city_table as (
                    SELECT route, MIN(city) as city
                    FROM t
                    WHERE city_rating IN (SELECT max(city_rating) FROM t WHERE t.route = route GROUP BY route)
                    GROUP BY route
                    ORDER BY route),
                    
                    sight_table as (
                    SELECT route, MIN(sight) as sight
                    FROM t
                    WHERE sight_rating IN (SELECT max(sight_rating) FROM t WHERE t.route = route GROUP BY route)
                    GROUP BY route
                    ORDER BY route),
                    
                    photo_table as (
                    SELECT route, MIN(photo_id) as photo_id
                    FROM t
                    WHERE photo_rating IN (SELECT max(photo_rating) FROM t WHERE t.route = route GROUP BY route)
                    GROUP BY route
                    ORDER BY route
                    )
                    
                    SELECT traces.title, city.city, sight.sight, photo.photo_id
                    FROM traces_routebycities traces
                    JOIN city_table city 
                    ON traces.id = city.route
                    JOIN sight_table sight
                    ON city.route = sight.route
                    JOIN photo_table photo
                    ON sight.route = photo.route;
                '''
            )
            data = cursor.fetchall()
            context = []
            for x in data:
                dictionary = dict()
                add_item(dictionary, 'trace', x[0])
                add_item(dictionary, 'city', x[1])
                add_item(dictionary, 'sight', x[2])
                add_item(dictionary, 'photo', x[3])
                context.append(dictionary)

        return render(request, self.template_name, {'context': context})
