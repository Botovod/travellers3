import psycopg2
import logging
import os

from django.conf import settings
from psycopg2 import OperationalError

path_to_log = os.path.join(os.path.dirname(__file__), "info.log")
logging.basicConfig(filename=path_to_log, filemode='w', level=logging.INFO)


class Connect:

    def __init__(self, modul):
        self.modul = modul

    def get_data(self):
        return self.modul


class ConnPsql:

    def __init__(self, modul=Connect(psycopg2)):
        self.modul = modul.get_data()

    def __enter__(self):
        self.conn = self.modul.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            host=settings.DATABASES['default']['HOST'],
            password=settings.DATABASES['default']['PASSWORD']
        )
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
        if exc_val:
            logging
            raise OperationalError
