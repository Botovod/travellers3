from django.urls import path
from .views import regions, region_detail

urlpatterns = [
    path('', regions, name='regions_url'),
    path('region/<int:id>/', region_detail, name='region_detail_url'),
]
