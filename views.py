from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.shortcuts import redirect

from .models import Przewoznicy, Kierowcy, Motorniczy, Linie
from .models import Przystanki, Autobusy, Tramwaje
from .forms import PrzewoznicyForm

# Create your views here.

def index(request):
    strony = [ 'autobusy', 'kierowcy', 'linie', 'przewoznicy', ]
    return render(request, 'index.html.j2', {'strony' : strony, })
#    return HttpResponse("Hello, world. You're at the polls index.")

def przewoznicy_edycja(request, nip):
    przewoznik = get_object_or_404(Przewoznicy, nip=nip)
    if request.method == "POST":
        form = PrzewoznicyForm(request.POST, instance = przewoznik)
        if form.is_valid():
            form.save()
            return redirect('.')
    else:
        form = PrzewoznicyForm(instance = przewoznik)
    return render(request, 'przewoznicy/edycja.html.j2', {'form': form})

def przewoznicy_nowy(request):
    if request.method == "POST":
        form = PrzewoznicyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    else:
        form = PrzewoznicyForm()
    return render(request, 'przewoznicy/edycja.html.j2', {'form': form})


class PrzewoznicyDetailView(generic.DetailView):
    model = Przewoznicy
    template_name = 'przewoznicy/detail.html.j2'

#    def get_object(self):
#        return get_object_or_404(Przewoznicy, nip=self.request.przewoznicy)


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
