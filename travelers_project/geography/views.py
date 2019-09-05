from django.shortcuts import render, get_object_or_404
from .models import City, Sight, Region


def regions(request):
    regions = Region.objects.all()
    context = {'regions': regions}
    return render(request, 'geography/regions.html', context)


def region_detail(request, id):
    region = get_object_or_404(Region, id=id)
    context = {'region': region}
    return render(request, 'geography/region_detail.html', context)


def city_detail(request, id):
    city = get_object_or_404(City, id=id)
    context = {'city': city}
    return render(request, 'geography/city_detail.html', context)
