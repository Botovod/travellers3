from rest_framework import serializers

from geography.models import Region
from geography.models import City
from geography.models import Sight
from geography.models import TypeOfSights
from geography.models import SectionOfSights


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


class SightListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sight
        fields = '__all__'


class SightDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sight
        fields = '__all__'


class TypeOfSightsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfSights
        fields = '__all__'


class TypeOfSightsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfSights
        fields = '__all__'


class SectionOfSightsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionOfSights
        fields = '__all__'


class SectionOfSightsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionOfSights
        fields = '__all__'
