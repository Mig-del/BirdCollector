from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #res.send in express
from .models import Bird





def home(request):
    return HttpResponse('<h1>Hello World!</>')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html', {'bird': bird})
