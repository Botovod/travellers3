from django.shortcuts import render
from .models import City, Sight, Region


def regions(request):
    regions = Region.objects.all()
    context = {'regions': regions}
    return render(request, 'geography/regions.html', context)
