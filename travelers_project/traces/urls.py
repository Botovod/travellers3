from django.urls import path, include
from rest_framework import routers

from traces.views_list.views import RouteByCitiesDetail
from traces.views_list.views import RouteByCitiesList
from traces.views_list.views import RouteBySightsDetail
from traces.views_list.views import RouteBySightsList

from traces.views_list.view_sets import (
    RouteByCitiesViewSet,
    CitiesRelationshipViewSet,
    RouteBySightsViewSet,
    SightsRelationshipViewSet,
)

router = routers.DefaultRouter()
router.register('router_by_cities', RouteByCitiesViewSet, basename='router_by_city')
router.register('cities_relations', CitiesRelationshipViewSet, basename='city_relation')
router.register('router_by_sights', RouteBySightsViewSet, basename='router_by_sight')
router.register('sights_relations', SightsRelationshipViewSet, basename='sight_relation')

urlpatterns = [
    # ex: traces/route_cities
    path('route-cities/', RouteByCitiesList.as_view(), name='routes-cities-list-url'),
    # ex: traces/route_cities/1/
    path('route-cities/<int:pk>/', RouteByCitiesDetail.as_view(), name='routes-cities-detail-url'),
    # ex: traces/route_sigths
    path('route-sights/', RouteBySightsList.as_view(), name='routes-sights-list-url'),
    # ex: traces/route_sights/1/
    path('route-sights/<int:pk>/', RouteBySightsDetail.as_view(), name='routes-detail-list-url'),
    # api/v1
    path('api/v1/', include(router.urls))
]
