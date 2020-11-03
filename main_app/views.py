from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dog, Toy
from .forms import WalkingForm, DogForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# ----------------- DOG INDEX
@login_required
def dogs_index(request):
    dogs = Dog.objects.filter(user=request.user)

    return render(request, 'dogs/index.html', { 'dogs': dogs })  

# ----------------- DOG DETAIL
@login_required
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

@login_required
def unused_toy(request, dog_id, toy_id):
    dog = Dog.objects.get(id=dog_id)
    toy = Toy.objects.get(id=toy_id)
    dog.toys.add(toy)
    return redirect('detail', dog_id)

# ----------------- DOG TOYS 

@login_required
def dogs_toy(request, dog_id, toy_id):
    dog = Dog.objects.get(id=dog_id)
    toy = Toy.objects.get(id=toy_id)
    dog.toys.add(toy)
    return redirect('detail', dog_id)

# ----------------- ADD A WALK

@login_required
def add_walking(request, dog_id):
    form = WalkingForm(request.POST)
    
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.dog_id = dog_id
        new_form.save()
    return redirect('detail', dog_id=dog_id)   


# ----------------- ADD A DOG

@login_required
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

# ----------------- EDIT A DOG

@login_required
def edit_dog(request, dog_id):
    dog = Dog.objects.get(id=dog_id)

    if request.method == 'POST':
        dog_form = DogForm(request.POST, instance=dog)
        if dog_form.is_valid():
            updated_dog = dog_form.save()
            return redirect('detail', updated_dog.id)
    else:
        form = DogForm(instance=dog)
        context = {'form': form, 'dog': dog}
        return render(request, 'dogs/edit.html', context)   


# ----------------- DELETE A DOG

@login_required
def delete_dog(request, dog_id):
    Dog.objects.get(id=dog_id).delete()
    return redirect('index')

# ----------------- SIGN UP

@login_required
def signup(request):
    error_message = ''

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dogs_index')
        else:
            error_message = 'Invalid sign up -- please try again'
            
        form = UserCreationForm()
            
        context = {'form': form, 'error_message': error_message}
        return render(request, 'regstration/signup.html', context)

          
