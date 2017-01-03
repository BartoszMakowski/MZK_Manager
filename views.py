from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Przewoznicy, Kierowcy, Motorniczy, Linie
from .models import Przystanki, Autobusy, Tramwaje

# Create your views here.

def index(request):
    strony = [ 'autobusy', 'kierowcy', 'linie', 'przewoznicy', ]
    return render(request, 'index.html.j2', {'strony' : strony, })
#    return HttpResponse("Hello, world. You're at the polls index.")


class PrzewoznicyListView(generic.ListView):
    model = Przewoznicy
    template_name = 'przewoznicy/index.html.j2'

class LinieListView(generic.ListView):
    model = Linie
    template_name = 'linie/index.html.j2'

class KierowcyListView(generic.ListView):
    model = Kierowcy
    template_name = 'kierowcy/index.html.j2'

class MotorniczyListView(generic.ListView):
    model = Motorniczy
    template_name = 'motorniczy/index.html.j2'

class PrzystankiListView(generic.ListView):
    model = Przystanki
    template_name = 'przystanki/index.html.j2'

class AutobusyListView(generic.ListView):
    model = Autobusy
    template_name = 'autobusy/index.html.j2'

class TramwajeListView(generic.ListView):
    model = Tramwaje
    template_name = 'tramwaje/index.html.j2'
