from django.db import models

# Create your models here.

class Dog:
    def __init__(self, name, breed, description, age, favetoy):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age
        self.favetoy = favetoy

dogs = [
    Dog('Tank', 'American Bulldog', 'Goofy little bulldozer of a dog', 5, 'squeaky toys'),
    Dog('Missy', 'Beagle', 'Funny and terrified of cats', 3, 'Gator!'),
    Dog('Baxter', 'Terrier', 'Can speak to bears', 6, 'Sticks')
]