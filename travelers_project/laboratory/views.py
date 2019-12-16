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
                FROM geography_region),
                
                best_cities as
                (WITH cities as 
                (SELECT region_id, max(rating) as city_rating
                FROM geography_city
                GROUP BY region_id)
                SELECT city.region_id, min(city.title) as city
                FROM cities
                LEFT JOIN geography_city city
                ON cities.region_id = city.region_id
                AND cities.city_rating = city.rating
                GROUP BY city.region_id),
                
                sights as 
                (WITH best_sights as 
                (WITH sights as 
                (SELECT city_id, max(rating) as sight_rating
                FROM geography_sight
                GROUP BY city_id)
                SELECT sight.city_id, min(sight.title) as sight
                FROM sights
                LEFT JOIN geography_sight sight
                ON sights.city_id = sight.city_id
                AND sights.sight_rating = sight.rating
                GROUP BY sight.city_id)
                
                SELECT city.region_id, min(best_sights.sight) as sight
                FROM geography_city city
                LEFT JOIN best_sights
                ON city.id = best_sights.city_id
                GROUP BY city.region_id),
                
                photos as 
                (WITH best_photos as
                (WITH photos as 
                (SELECT sight_id, max(rating) as photo_rating
                FROM geography_sightphoto
                GROUP BY sight_id)
                
                SELECT photo.sight_id, min(photo.id) as photo
                FROM photos
                LEFT JOIN geography_sightphoto photo
                ON photos.sight_id = photo.sight_id
                AND photos.photo_rating = photo.rating
                GROUP BY photo.sight_id)
                
                SELECT city.region_id,  min(best_photos.photo) photo
                FROM geography_city city
                RIGHT JOIN geography_sight sight
                ON city.id = sight.city_id
                RIGHT JOIN best_photos
                ON sight.id = best_photos.sight_id
                GROUP BY city.region_id)
                
                SELECT regions.id, regions.title, best_cities.city, sights.sight, photos.photo
                FROM regions
                LEFT JOIN best_cities
                ON regions.id = best_cities.region_id
                LEFT JOIN sights
                ON regions.id = sights.region_id
                LEFT JOIN photos
                ON regions.id = photos.region_id
                ORDER BY regions.id;
                '''
            )
            data = cursor.fetchall()
            context = []
            for x in data:
                dictionary = dict()
                add_item(dictionary, 'region', x[1])
                add_item(dictionary, 'city', x[2])
                add_item(dictionary, 'sight', x[3])
                add_item(dictionary, 'photo', x[4])
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
