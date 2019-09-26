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

    def get_context_data(self, **kwargs):
        object_list = City.objects.filter(region=self.get_object())
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class CityList(ListView):
    model = City
    template_name = 'geography/city_list.html'
    context_object_name = 'city_list'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        s = """There are many variations of passages of Lorem Ipsum available,
            but the majority have suffered alteration in some form, by injected humour, or randomised word.
            Richard McClintock."""
        context = super(CityList, self).get_context_data(*args, **kwargs)
        context['mock_text'] = s
        return context


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
