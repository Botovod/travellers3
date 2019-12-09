from rest_framework import serializers
from traces.models import (
    RouteByCities,
    CitiesRelationship,
    RouteBySights,
    SightsRelationship,
)


class RouteByCitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteByCities
        fields = ('id', 'title', 'description', 'cities')


class CitiesRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitiesRelationship
        fields = ('id', 'city', 'route', 'position')


class RouteBySightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteBySights
        fields = ('id', 'title', 'sights', 'description')


class SightsRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = SightsRelationship
        fields = ('id', 'sight', 'route', 'position')
