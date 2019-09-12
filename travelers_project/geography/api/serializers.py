from rest_framework import serializers

from geography.models import Region
from geography.models import City


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class RegionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
