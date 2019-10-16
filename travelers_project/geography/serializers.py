from rest_framework import serializers

from geography.models import City, Region, Sight


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'title', 'description',)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'title', 'description', 'region',)


class SightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sight
        fields = ('id', 'title', 'type', 'text', 'city', 'latitude', 'longitude')
