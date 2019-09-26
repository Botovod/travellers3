from django.contrib import admin

from .models import RouteByCities
from .models import RouteBySights

admin.site.register(RouteByCities)
admin.site.register(RouteBySights)
