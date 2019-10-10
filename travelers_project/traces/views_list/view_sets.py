from rest_framework import viewsets
from traces.models import (
    RouteByCities,
    CitiesRelationship,
    RouteBySights,
    SightsRelationship,
)
from traces.serializers import (
    RouteByCitiesSerializer,
    CitiesRelationshipSerializer,
    RouteBySightsSerializer,
    SightsRelationshipSerializer,
)


class RouteByCitiesViewSet(viewsets.ModelViewSet):
    queryset = RouteByCities.objects.all()
    serializer_class = RouteByCitiesSerializer


class CitiesRelationshipViewSet(viewsets.ModelViewSet):
    queryset = CitiesRelationship.objects.all()
    serializer_class = CitiesRelationshipSerializer


class RouteBySightsViewSet(viewsets.ModelViewSet):
    queryset = RouteBySights.objects.all()
    serializer_class = RouteBySightsSerializer


class SightsRelationshipViewSet(viewsets.ModelViewSet):
    queryset = SightsRelationship.objects.all()
    serializer_class = SightsRelationshipSerializer
