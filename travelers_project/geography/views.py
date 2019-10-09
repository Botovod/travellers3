from django.views.generic.detail import DetailView
from django.views.generic.list import MultipleObjectMixin, ListView
from rest_framework import generics

from geography.models import City, Sight, Region
from geography.models import TypeOfSights, SightPhoto, SectionOfSights

from geography.serializers import RegionListSerializer, RegionDetailSerializer
from geography.serializers import CityListSerializer, CityDetailSerializer
from geography.serializers import SightListSerializer, SightDetailSerializer
from geography.serializers import SightPhotoListSerializer, SightPhotoDetailSerializer
from geography.serializers import SectionOfSightsListSerializer, SectionOfSightsDetailSerializer
from geography.serializers import TypeOfSightsListSerializer, TypeOfSightsDetailSerializer


class RegionList(ListView):
    model = Region
    template_name = 'geography/regions.html'
    context_object_name = 'region_list'
    paginate_by = 10


class RegionDetail(DetailView, MultipleObjectMixin):
    model = Region
    template_name = 'geography/region_detail.html'
    context_object_name = 'region_detail'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        object_list = City.objects.filter(region=self.get_object())
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class CityList(ListView):
    model = City
    template_name = 'geography/city_list.html'
    context_object_name = 'city_list'
    paginate_by = 12


class CityDetail(DetailView):
    model = City
    template_name = 'geography/city_detail.html'
    context_object_name = 'city_detail'


class SightList(ListView):
    model = Sight
    template_name = 'geography/sight_list.html'
    context_object_name = 'sight_list'
    paginate_by = 12


class SightDetail(DetailView):
    model = Sight
    template_name = 'geography/sight_detail.html'
    context_object_name = 'sight_detail'


# api views

class RegionListAPI(generics.ListCreateAPIView):
    queryset = Region.objects.order_by('id')
    serializer_class = RegionListSerializer


class RegionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionDetailSerializer


class CityListAPI(generics.ListCreateAPIView):
    queryset = City.objects.order_by('id')
    serializer_class = CityListSerializer


class CityDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer


class SightListAPI(generics.ListCreateAPIView):
    queryset = Sight.objects.order_by('id')
    serializer_class = SightListSerializer


class SightDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sight.objects.all()
    serializer_class = SightDetailSerializer


class SightPhotoListAPI(generics.ListCreateAPIView):
    queryset = SightPhoto.objects.order_by('id')
    serializer_class = SightPhotoListSerializer


class SightPhotoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = SightPhoto.objects.all()
    serializer_class = SightPhotoDetailSerializer


class SectionOfSightsListAPI(generics.ListCreateAPIView):
    queryset = SectionOfSights.objects.order_by('id')
    serializer_class = SectionOfSightsListSerializer


class SectionOfSightsDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = SectionOfSights.objects.all()
    serializer_class = SectionOfSightsDetailSerializer


class TypeOfSightsListAPI(generics.ListCreateAPIView):
    queryset = TypeOfSights.objects.order_by('id')
    serializer_class = TypeOfSightsListSerializer


class TypeOfSightsDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeOfSights.objects.all()
    serializer_class = TypeOfSightsDetailSerializer
