from django.contrib import admin
from .models import Traveler, CityTrip, SightTrip

admin.site.register(Traveler)
admin.site.register(CityTrip)
admin.site.register(SightTrip)
