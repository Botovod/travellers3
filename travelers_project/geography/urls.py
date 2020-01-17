from rest_framework.routers import SimpleRouter

from django.urls import path
from geography.views import RegionList, RegionDetail, CityList, CityDetail, SightList, SightDetail
from geography.views import RegionViewSet, CityViewSet, SightViewSet, SightCityDetail
from geography.views import SightPhotoViewSet, SectionOfSightsViewSet, TypeOfSightsViewSet

from geography.views import RouteByCitiesViewSet, RouteBySightsViewSet
from geography.views import CitiesRelationshipViewSet, SightsRelationshipViewSet, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index_url'),
    path('regions/', RegionList.as_view(), name='region_list_url'),
    path('regions/<int:pk>/', RegionDetail.as_view(), name='region_detail_url'),
    path('cities/', CityList.as_view(), name='city_list_url'),
    path('cities/<int:pk>/', CityDetail.as_view(), name='city_detail_url'),
    # path('sights/', SightList.as_view(), name='sight_list_url'),
    path('sights/<int:pk>/', SightDetail.as_view(), name='sight_detail_url'),
    path('sights/', SightCityDetail.as_view(), name='sight_list_with_cities_url'),

]

router = SimpleRouter()
router.register('api/v1/regions', RegionViewSet, base_name='regions')
router.register('api/v1/cities', CityViewSet, base_name='cities')
router.register('api/v1/sights', SightViewSet, base_name='sights')
router.register('api/v1/sightphotos', SightPhotoViewSet, base_name='sightphotos')
router.register('api/v1/sectionofsights', SectionOfSightsViewSet, base_name='sectionofsights')
router.register('api/v1/typeofsights', TypeOfSightsViewSet, base_name='typeofsights')

router.register('api/v1/router_by_cities', RouteByCitiesViewSet, basename='router_by_city')
router.register('api/v1/cities_relations', CitiesRelationshipViewSet, basename='city_relation')
router.register('api/v1/router_by_sights', RouteBySightsViewSet, basename='router_by_sight')
router.register('api/v1/sights_relations', SightsRelationshipViewSet, basename='sight_relation')

urlpatterns.extend(router.urls)
