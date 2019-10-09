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
        fields = '__all__'

class CitiesRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitiesRelationship
        fields = '__all__'

class RouteBySightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteBySights
        fields = '__all__'

class SightsRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = SightsRelationship
        fields = '__all__'
