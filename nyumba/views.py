from . models import NeighbourHood, Profile, Business
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="/accounts/register")
def neighbourhood(request):
    if request.user.is_authenticated:
        if Join.objects.filter(user_id=request.user).exists():
            hood = Neighbourhood.objects.get(pk=request.user.join.hood_id.id)

            return render(request, 'hood/myhood.html', {"hood":hood, "posts":posts, "business":business, "comments":comments})
        else:
            neighbourhoods = Neighbourhood.objects.all()
            return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login/')
def create_hood(request):
    """
    View to create an instance of a neighbourhood
    """
    if request.method == 'POST':
        form = CreateHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = request.user
            hood.save()
            return redirect('index')
    else:
        form = CreateHoodForm()
        return render(request, 'hood/create_hood.html', locals())
