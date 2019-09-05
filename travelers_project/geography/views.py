from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import City, Sight, Region, TypeOfSights


class RegionList(ListView):
    model = Region
    template_name = 'geography/regions.html'
    context_object_name = 'region_list'
region_list = RegionList.as_view()


class RegionDetail(DetailView):
    model = Region
    template_name = 'geography/region_detail.html'
    context_object_name = 'region_detail'
region_detail = RegionDetail.as_view()


class CityDetail(DetailView):
    model = City
    template_name = 'geography/city_detail.html'
    context_object_name = 'city_detail'
city_detail = CityDetail.as_view()


class TypeOfSightsList(ListView):
    model = TypeOfSights
    template_name = 'geography/type_sights.html'
    context_object_name = 'type_sights'
type_sights = TypeOfSightsList.as_view()


class TypeOfSightsDetail(DetailView):
    model = TypeOfSights
    template_name = 'geography/type_sight_detail.html'
    context_object_name = 'type_sight_detail'
type_sight_detail = TypeOfSightsDetail.as_view()
