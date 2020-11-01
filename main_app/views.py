from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog, Toy
from .forms import WalkingForm, DogForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# ----------------- DOG INDEX

def dogs_index(request):
    dogs = Dog.objects.all()

    return render(request, 'dogs/index.html', { 'dogs': dogs })  

# ----------------- DOG DETAIL

def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)

    unused_toys = Toy.objects.exclude(id__in=dog.toys.all().values_list('id'))
    
    walking_form = WalkingForm()   
    
    return render(request, 'dogs/detail.html', { 
        'dog': dog, 
        'walking_form': walking_form,
        'toys': unused_toys 
    }) 

# ----------------- DOG UNUSED TOYS

def unused_toy(request, dog_id, toy_id):
    dog = Dog.objects.get(id=dog_id)
    toy = Toy.objects.get(id=toy_id)
    dog.toys.add(toy)
    return redirect('detail', dog_id)

# ----------------- DOG TOYS 

def dogs_toy(request, dog_id, toy_id):
    dog = Dog.objects.get(id=dog_id)
    toy = Toy.objects.get(id=toy_id)
    dog.toys.add(toy)
    return redirect('detail', dog_id)

# ----------------- ADD A WALK

def add_walking(request, dog_id):
    form = WalkingForm(request.POST)
    
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.dog_id = dog_id
        new_form.save()
    return redirect('detail', dog_id=dog_id)   


# ----------------- ADD A DOG

def add_dog(request):
    if request.method == 'POST':
        dog_form = DogForm(request.POST)
        if dog_form.is_valid():
            new_dog = dog_form.save(commit=False)
            new_dog.user = request.user
            new_dog.save()

            return redirect('detail', new_dog.id)

    else: 
        form = DogForm()
        context = {'form': form}
        return render(request, 'dogs/new.html', context)        
