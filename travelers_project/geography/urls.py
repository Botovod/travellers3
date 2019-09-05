from django.urls import path
from .views import regions, region_detail, city_detail, type_sights

urlpatterns = [
    path('', regions, name='regions_url'),
    path('region/<int:id>/', region_detail, name='region_detail_url'),
    path('city/<int:id>/', city_detail, name='city_detail_url'),
    path('type-sights/', type_sights, name='type_sights_url'),
]
