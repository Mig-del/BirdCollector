from django.shortcuts import render, redirect

# import the CreateView class
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
from django.http import HttpResponse #res.send in express
from .models import Bird
from .forms import FeedingForm


## the template the CreateView and the UpdateVIew use is the same
# templates/<app_name>/<model>_form.html
# templates/main_app/cat_form.html
class BirdCreate(CreateView):
	model = Bird
	fields = '__all__'# this is two underscores

class BirdUpdate(UpdateView):
  model = Bird # we dont want to let anyone change Birds name, so lets not include the name in the fields
  fields = ['specie', 'description', 'age']
  # where's the redirect defined at for a put request?

class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds/' # because our model is redirecting to specific cat but we just deleted it





def home(request):
    return HttpResponse('<h1>Hello World!</>')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    feeding_form = FeedingForm()
    return render(request, 'birds/detail.html', {'bird': bird, 'feeding_form': feeding_form})

def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
      new_feeding = form.save(commit=False)
      new_feeding.bird_id = bird_id
      new_feeding.save()
      return redirect('detail', bird_id=bird_id)

