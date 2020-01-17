from django.views.generic.detail import DetailView
from django.views.generic.list import MultipleObjectMixin, ListView
from django.views.generic import TemplateView

from rest_framework import viewsets

from geography.models import Region, City, Sight, SightPhoto, SectionOfSights, TypeOfSights
from geography.serializers import RegionSerializer, CitySerializer, SightSerializer
from geography.serializers import SightPhotoSerializer, SectionOfSightsSerializer, TypeOfSightsSerializer

from traces.models import RouteByCities, CitiesRelationship, RouteBySights, SightsRelationship
from geography.serializers import RouteByCitiesSerializer, RouteBySightsSerializer
from geography.serializers import CitiesRelationshipSerializer, SightsRelationshipSerializer

class IndexView(TemplateView):
    template_name = "geography/index.html"

class RegionList(ListView):
    model = Region
    template_name = 'geography/regions.html'
    context_object_name = 'region_list'
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sights'] = Sight.objects.all()[:4]
        return context


class RegionDetail(DetailView, MultipleObjectMixin):
    model = Region
    template_name = 'geography/region_detail.html'
    context_object_name = 'region_detail'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        object_list = City.objects.filter(region=self.get_object())
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class CityList(ListView):
    model = City
    template_name = 'geography/city_list.html'
    context_object_name = 'city_list'
    paginate_by = 8

class SightCityDetail(ListView):
    # model = City
    queryset = City.objects.order_by('-rating')
    template_name = 'geography/sight_with_city_list.html'
    context_object_name = 'sight_city_detail'
    paginate_by = 8


class CityDetail(DetailView):
    model = City
    template_name = 'geography/city_detail.html'
    context_object_name = 'city_detail'


class SightList(ListView):
    model = Sight
    template_name = 'geography/sight_list.html'
    context_object_name = 'sight_list'
    paginate_by = 9


class SightDetail(DetailView):
    model = Sight
    template_name = 'geography/sight_detail.html'
    context_object_name = 'sight_detail'

# api views
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SightViewSet(viewsets.ModelViewSet):
    queryset = Sight.objects.all()
    serializer_class = SightSerializer


class SightPhotoViewSet(viewsets.ModelViewSet):
    queryset = SightPhoto.objects.all()
    serializer_class = SightPhotoSerializer


class SectionOfSightsViewSet(viewsets.ModelViewSet):
    queryset = SectionOfSights.objects.all()
    serializer_class = SectionOfSightsSerializer


class TypeOfSightsViewSet(viewsets.ModelViewSet):
    queryset = TypeOfSights.objects.all()
    serializer_class = TypeOfSightsSerializer


class RouteByCitiesViewSet(viewsets.ModelViewSet):
    queryset = RouteByCities.objects.all()
    serializer_class = RouteByCitiesSerializer


class CitiesRelationshipViewSet(viewsets.ModelViewSet):
    queryset = CitiesRelationship.objects.all()
    serializer_class = CitiesRelationshipSerializer


class RouteBySightsViewSet(viewsets.ModelViewSet):
    queryset = RouteBySights.objects.all()
    serializer_class = RouteBySightsSerializer


class SightsRelationshipViewSet(viewsets.ModelViewSet):
    queryset = SightsRelationship.objects.all()
    serializer_class = SightsRelationshipSerializer
