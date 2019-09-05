from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Traveler


def index(request):
    traveler_list = Traveler.objects.all()
    context = {
        'traveler_list': traveler_list,
    }
    return render(request, 'travelers/index.html', context)


def traveler_detail(request, traveler_id):
    traveler = get_object_or_404(Traveler, pk=traveler_id)
    return render(request,
                  'travelers/traveler_detail.html',
                  {'traveler': traveler},
                  )
