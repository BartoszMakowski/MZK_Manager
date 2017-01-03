from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html.j2')
#    return HttpResponse("Hello, world. You're at the polls index.")
