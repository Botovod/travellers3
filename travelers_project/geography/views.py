from django.views.generic.detail import DetailView
from django.views.generic.list import MultipleObjectMixin, ListView

from geography.models import City, Sight, Region, TypeOfSights, SightPhoto


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

    def get_context_data(self, **kwrags):
        object_list = City.objects.filter(region=self.get_object())
        context = super().get_context_data(object_list=object_list, **kwrags)
        return context


class CityList(ListView):
    model = City
    template_name = 'geography/city_list.html'
    context_object_name = 'city_list'
    paginate_by = 10


class CityDetail(DetailView):
    model = City
    template_name = 'geography/city_detail.html'
    context_object_name = 'city_detail'


class SightList(ListView):
    model = Sight
    template_name = 'geography/sight_list.html'
    context_object_name = 'sight_list'


class SightDetail(DetailView):
    model = Sight
    template_name = 'geography/sight_detail.html'
    context_object_name = 'sight_detail'


