from django.urls import path, include
from rest_framework.routers import SimpleRouter

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

urlpatterns = [
    path('route-cities/', RouteByCitiesList.as_view(), name='routes-cities-list-url'),
    path('route-cities/<int:pk>/', RouteByCitiesDetail.as_view(), name='routes-cities-detail-url'),
    path('route-sights/', RouteBySightsList.as_view(), name='routes-sights-list-url'),
    path('route-sights/<int:pk>/', RouteBySightsDetail.as_view(), name='routes-sights-detail-url'),
]

router = SimpleRouter()
router.register('api/v1/router_by_cities', RouteByCitiesViewSet, basename='router_by_city')
router.register('api/v1/cities_relations', CitiesRelationshipViewSet, basename='city_relation')
router.register('api/v1/router_by_sights', RouteBySightsViewSet, basename='router_by_sight')
router.register('api/v1/sights_relations', SightsRelationshipViewSet, basename='sight_relation')

urlpatterns.extend(router.urls)
