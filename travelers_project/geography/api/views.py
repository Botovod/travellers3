from rest_framework import generics

from geography.models import City
from geography.models import Region

from geography.api.serializers import RegionListSerializer
from geography.api.serializers import RegionDetailSerializer
from geography.api.serializers import CityListSerializer
from geography.api.serializers import CityDetailSerializer


class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.order_by('id')
    serializer_class = RegionListSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDetailSerializer


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.order_by('id')
    serializer_class = CityListSerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer
