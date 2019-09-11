from rest_framework import generics

from geography.models import Region

from geography.api.serializers import RegionListSerializer
from geography.api.serializers import RegionDetailSerializer


class RegionList(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer


class RegionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDetailSerializer

