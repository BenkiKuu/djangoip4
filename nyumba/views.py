from . models import NeighbourHood, Profile, Business, JoinHood, Allert, Comment
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .forms import CreateHoodForm, CreateBusinessForm, CreateAllertForm, CommentForm
# Create your views here.


@login_required(login_url="/accounts/register")
def neighbourhood(request):
    if request.user.is_authenticated:
        if JoinHood.objects.filter(user_id=request.user).exists():
            hood = NeighbourHood.objects.get(pk=request.user.joinhood.hood_id.id)
            allert = Allert.objects.filter(hood = request.user.joinhood.hood_id.id)
            business = Business.objects.filter(hood = request.user.joinhood.hood_id.id)
            comments = Comment.objects.all()
            return render(request, 'myhood.html', locals())
        else:
            neighbourhoods = NeighbourHood.objects.all()
            return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):

    if request.method == 'POST':
        form = CreateHoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user
            hood.save()
            return redirect('home')
    else:
        form = CreateHoodForm()
        return render(request, 'forms/new_neighbourhood.html', locals())

@login_required(login_url='/accounts/login/')
def join_hood(request, hoodId):

    neighbourhood = NeighbourHood.objects.get(pk=hoodId)
    if JoinHood.objects.filter(user_id=request.user).exists():
        JoinHood.objects.filter(user_id=request.user).update(hood_id=neighbourhood)
    else:
        JoinHood(user_id=request.user, hood_id=neighbourhood).save()
    return redirect('home')

@login_required(login_url='/accounts/login/')
def exithood(request,hoodId):

	if JoinHood.objects.filter(user_id = request.user).exists():
	       JoinHood.objects.get(user_id = request.user).delete()
	return redirect('index')

@login_required(login_url='/accounts/login/')
def create_business(request):

    if JoinHood.objects.filter(user_id = request.user).exists():
        if request.method == 'POST':
            form = CreateBusinessForm(request.POST)
            if form.is_valid():
                business = form.save(commit=False)
                business.user = request.user
                business.location = request.user.join.hood_id
                business.save()
                return redirect('index')
        else:
            form = CreateBusinessForm()
            return render(request, 'create_business.html', locals())


@login_required(login_url='/accounts/login/')
def post_allert(request):

    if JoinHood.objects.filter(user_id = request.user).exists():
        if request.method == 'POST':
            form = CreateAllertForm(request.POST)
            if form.is_valid():
                allert = form.save(commit=False)
                allert.user = request.user
                allert.hood = request.user.join.hood_id
                allert.save()
                return redirect('index')
        else:
            form = CreatePostForm()
            return render(request, 'create_allert.html', locals())


@login_required(login_url='/accounts/login/')
def create_comment(request, post_id):

    if Join.objects.filter(user_id = request.user).exists():
        post = Post.objects.get(id = post_id)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
                return redirect('index')
        else:
            form = CommentForm()
            return render(request, 'create_comment.html', locals())
