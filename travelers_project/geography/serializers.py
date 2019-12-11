from rest_framework import serializers

from geography.models import City, Region, Sight, SightPhoto, SectionOfSights, TypeOfSights

from traces.models import RouteByCities, CitiesRelationship, RouteBySights, SightsRelationship


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


class SightPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SightPhoto
        fields = ('id', 'sight',)


class SectionOfSightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionOfSights
        fields = ('id', 'types', 'title',)


class TypeOfSightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfSights
        fields = ('id', 'title', 'marker',)




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