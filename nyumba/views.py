from . models import NeighbourHood, Profile, Business
from django.shortcuts import render

# Create your views here.
def neighbourhood(request):
    title = 'neighbourhoods'
    neighbourhoods = NeighbourHood.objects.all()
    return render(request, 'index.html', locals())
