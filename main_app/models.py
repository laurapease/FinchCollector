from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

WALKS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
            return self.name

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    age = models.IntegerField()
    favetoy = models.CharField(max_length=50)
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

    def walked_for_today(self):
        return self.walking_set.filter(date=date.today()).count() >= len(WALKS)    

class Walking(models.Model):
    date = models.DateField('date')
    note = models.CharField(max_length=50) 
    walk = models.CharField(
        max_length=1,
        choices=WALKS,
        default=WALKS[0][0]
    )

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)    

    def __str__(self):
        return f"{self.get_walk_display()} on {self.date}"

    class Meta:
        ordering = ['-date']    
