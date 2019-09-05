from django.urls import path
from .views import regions, region_detail, city_detail, type_sights, type_sight_detail

urlpatterns = [
    path('', regions, name='regions_url'),
    path('region/<int:id>/', region_detail, name='region_detail_url'),
    path('city/<int:id>/', city_detail, name='city_detail_url'),
    path('type-sights/', type_sights, name='type_sights_url'),
    path('type-sights/<int:id>/', type_sight_detail, name='type_sight_detail_url'),
]
