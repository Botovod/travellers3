import logging
import psycopg2

from django.conf import settings
from django.shortcuts import render
from psycopg2 import OperationalError

from django.views.generic.list import ListView


class TopCitiesList(ListView):
    template_name = 'laboratory/topcities.html'
    paginate_by = 10

    def get(self, request):
        regions = get_data()
        context = {'regions': regions}

        return render(request, template_name=self.template_name, context=context)


def get_data():
    regions = []
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
        cur.execute('''SELECT id, title 
                       FROM geography_region;''')
        regions_qs = cur.fetchall()
        for _, title in regions_qs:
            regions.append(title)

        conn.commit()
        cur.close()
    finally:
        conn.close()
    return regions
