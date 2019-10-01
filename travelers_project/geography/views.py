from django.views.generic.detail import DetailView
from django.views.generic.list import MultipleObjectMixin, ListView
from rest_framework import generics

from sorl.thumbnail import get_thumbnail

from travelers_project.settings import DEFAULT_PHOTO_PATH

from geography.models import City, Sight, Region
from geography.models import TypeOfSights, SightPhoto, SectionOfSights

from geography.serializers import RegionListSerializer, RegionDetailSerializer
from geography.serializers import CityListSerializer, CityDetailSerializer
from geography.serializers import SightListSerializer, SightDetailSerializer
from geography.serializers import SightPhotoListSerializer, SightPhotoDetailSerializer
from geography.serializers import SectionOfSightsListSerializer, SectionOfSightsDetailSerializer
from geography.serializers import TypeOfSightsListSerializer, TypeOfSightsDetailSerializer

mock_text = """There are many variations of passages of Lorem Ipsum available,
    but the majority have suffered alteration in some form, by injected humour, or randomised word.
    Richard McClintock."""


class RegionList(ListView):
    model = Region
    template_name = 'geography/regions.html'
    context_object_name = 'region_list'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(RegionList, self).get_context_data(*args, **kwargs)
        context['mock_text'] = mock_text

        try:
            file = open(DEFAULT_PHOTO_PATH)
            default_image = get_thumbnail(file, 'x100', crop='center')
            context['default_image'] = default_image
        except FileExistsError:
            pass

        return context


class RegionDetail(DetailView, MultipleObjectMixin):
    model = Region
    template_name = 'geography/region_detail.html'
    context_object_name = 'region_detail'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        object_list = City.objects.filter(region=self.get_object())
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['mock_text'] = mock_text

        try:
            file = open(DEFAULT_PHOTO_PATH)
            default_image = get_thumbnail(file, 'x150', crop='center')
            context['default_image'] = default_image
        except FileExistsError:
            pass

        return context


class CityList(ListView):
    model = City
    template_name = 'geography/city_list.html'
    context_object_name = 'city_list'
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super(CityList, self).get_context_data(*args, **kwargs)
        context['mock_text'] = mock_text

        try:
            file = open(DEFAULT_PHOTO_PATH)
            default_image = get_thumbnail(file, 'x150', crop='center')
            context['default_image'] = default_image
        except FileExistsError:
            pass

        return context


class CityDetail(DetailView):
    model = City
    template_name = 'geography/city_detail.html'
    context_object_name = 'city_detail'


class SightList(ListView):
    model = Sight
    template_name = 'geography/sight_list.html'
    context_object_name = 'sight_list'
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super(SightList, self).get_context_data(*args, **kwargs)
        context['mock_text'] = mock_text

        try:
            file = open(DEFAULT_PHOTO_PATH)
            default_image = get_thumbnail(file, 'x150', crop='center')
            context['default_image'] = default_image
        except FileExistsError:
            pass

        return context


class SightDetail(DetailView):
    model = Sight
    template_name = 'geography/sight_detail.html'
    context_object_name = 'sight_detail'


# api views

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


class SightList(generics.ListCreateAPIView):
    queryset = Sight.objects.order_by('id')
    serializer_class = SightListSerializer


class SightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sight.objects.all()
    serializer_class = SightDetailSerializer


class SightPhotoList(generics.ListCreateAPIView):
    queryset = SightPhoto.objects.order_by('id')
    serializer_class = SightPhotoListSerializer


class SightPhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SightPhoto.objects.all()
    serializer_class = SightPhotoDetailSerializer


class SectionOfSightsList(generics.ListCreateAPIView):
    queryset = SectionOfSights.objects.order_by('id')
    serializer_class = SectionOfSightsListSerializer


class SectionOfSightsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SectionOfSights.objects.all()
    serializer_class = SectionOfSightsDetailSerializer


class TypeOfSightsList(generics.ListCreateAPIView):
    queryset = TypeOfSights.objects.order_by('id')
    serializer_class = TypeOfSightsListSerializer


class TypeOfSightsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TypeOfSights.objects.all()
    serializer_class = TypeOfSightsDetailSerializer
