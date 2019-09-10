from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from geography.models import City, Sight, Region, TypeOfSights, SightPhoto


class RegionList(ListView):
    model = Region
    template_name = 'geography/regions.html'
    context_object_name = 'region_list'
    paginate_by = 4


class RegionDetail(DetailView):
    model = Region
    template_name = 'geography/region_detail.html'
    context_object_name = 'region_detail'


class CityList(ListView):
    model = City
    template_name = 'geography/city_list.html'
    context_object_name = 'city_list'
    paginate_by = 20


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
