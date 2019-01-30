from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Candidate, Position
from .forms import PostForm, PositionForm
from datetime import datetime
# Create your views here.

def index(request):
    context = {}
    candidate_names = Candidate.objects.all()
    context['candidate_names']=candidate_names
    return render(request, "index.html", context)

def detail(request, candidate_id):
    context = {}
    context['votes'] = Candidate.objects.get(id=candidate_id)
    return render(request, 'detail.html', context)

def create(request):
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            context['form'] = form
            return render(request, 'create.html', context)
    else:
        context['form'] = PostForm(initial={'birthdate': datetime.now().date()})
        return render(request, 'create.html', context)

def createposition(request):
    context = {}
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            context['form'] = form
            return render(request, 'createposition.html', context)
    else:
        context['form'] = PositionForm()
        return render(request, 'createposition.html', context)


def update(request, candidate_id):
    if request.method == 'POST':
        post = Candidate.objects.get(id=candidate_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        post = Candidate.objects.get(id=candidate_id)
        context = {}
        context['form'] = PostForm(instance=post)
        return render(request, 'update.html', context)
