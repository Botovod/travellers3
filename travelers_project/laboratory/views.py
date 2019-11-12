from django.shortcuts import render

from django.views.generic.list import ListView


class TopCitiesList(ListView):
    template_name = 'laboratory/topcities.html'

    def get(self, request):

        return render(request, template_name=self.template_name)
