from rest_framework import serializers

from geography.models import Region


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class RegionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

