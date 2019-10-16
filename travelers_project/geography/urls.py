from rest_framework.routers import SimpleRouter

from django.urls import path
from geography.views import RegionList, RegionDetail, CityList, CityDetail, SightList, SightDetail
from geography.views import RegionViewSet, CityViewSet, SightViewSet

urlpatterns = [
    path('', RegionList.as_view(), name='region_list_url'),
    path('regions/<int:pk>/', RegionDetail.as_view(), name='region_detail_url'),
    path('cities/', CityList.as_view(), name='city_list_url'),
    path('cities/<int:pk>/', CityDetail.as_view(), name='city_detail_url'),
    path('sights/', SightList.as_view(), name='sight_list_url'),
    path('sights/<int:pk>/', SightDetail.as_view(), name='sight_detail_url'),
]

router = SimpleRouter()
router.register('api/v1/regions', RegionViewSet, base_name='regions')
router.register('api/v1/cities', CityViewSet, base_name='cities')
router.register('api/v1/sights', SightViewSet, base_name='sights')

urlpatterns.extend(router.urls)
