from django.contrib import admin

from traces.models import RouteByCities
from traces.models import RouteBySights

admin.site.register(RouteByCities)
admin.site.register(RouteBySights)
