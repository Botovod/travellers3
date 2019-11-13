import logging
import psycopg2
import random
from psycopg2 import OperationalError

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        set_rating_all_objects()


def set_rating_all_objects():
    try:
        conn = psycopg2.connect(dbname=settings.DATABASES['default']['NAME'],
                                user=settings.DATABASES['default']['USER'],
                                host=settings.DATABASES['default']['HOST'],
                                password=settings.DATABASES['default']['PASSWORD']
                                )
    except (OperationalError, KeyError):
        logging.exception('Unable to open DB')
    else:
        cur = conn.cursor()
        cities = get_object(cur, 'geography_city')
        for _id, title in cities:
            set_rating(cur, 'geography_city', _id, title)

        sights = get_object(cur, 'geography_sight')
        for _id, title in sights:
            set_rating(cur, 'geography_sight', _id, title)

        photos = get_object(cur, 'geography_sightphoto')
        for _id, title in photos:
            set_rating(cur, 'geography_sightphoto', _id, title)

        conn.commit()
        cur.close()
        conn.close()


def get_random_number():
    return random.randint(1, 10)


def get_object(cursor, table):
    cursor.execute('''SELECT id, title 
                           FROM {}
                           WHERE rating = 0;'''.format(table))
    cities = cursor.fetchall()
    return cities


def set_rating(cursor, table, _id, title):
    rating = get_random_number()
    try:
        cursor.execute('''UPDATE {} 
                          SET rating = {}
                          WHERE id = {};'''.format(table, rating, _id))
        print('{} присвоен рейтинг {}'.format(title, rating))
    except psycopg2.errors.NotNullViolation:
        print('{} не присвоен рейтинг'.format(title))
