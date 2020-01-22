from django.views.generic import ListView
from .models import MainPage


class IndexView(ListView):
    model = MainPage
    template_name = "mainpage/index.html"
    context_object_name = 'main_page'
