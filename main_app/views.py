from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #res.send in express

class Bird:
    def __init__(self, name, specie, description, age):
        self.name = name
        self.specie = specie
        self.description = description
        self.age = age


birds = [
    Bird('Zazu', 'African red-billed hornbill', 'from Lion King', 'Adult'),
    Bird('Slinky', 'Parrot', 'colorful red, blue and green', 'Juvenile'),
    Bird('Scooter', 'Hummingbird', 'long beak, shiny green belly', 0),
    Bird('Rio', 'Macaw', 'multiple colors red, green, orange, yellow', 'Adult'),
    Bird('Tweety', 'Yellow canary', 'yellow, black feathers', 'Juvenile')
]




def home(request):
    return HttpResponse('<h1>Hello World!</>')

def about(request):
    return render(request, 'about.html')

def birds_index(request):
    return render(request, 'birds/index.html', {'birds': birds})
