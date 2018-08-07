from . models import NeighbourHood, Profile, Business
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def neighbourhood(request):
    title = 'neighbourhoods'
    neighbourhoods = NeighbourHood.objects.all()
    return render(request, 'index.html', locals())
