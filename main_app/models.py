from django.db import models

# Create your models here.

WALKS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    age = models.IntegerField()
    favetoy = models.CharField(max_length=50)

    def _str__(self):
        return self.name

class Walking(models.Model):
    date = models.DateField('walking date')
    note = models.CharField(max_length=50) 
    walk = models.CharField(
        max_length=1,
        choices=WALKS,
        default=WALKS[0][0]
    )

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)    

    def __str__(self):
        return f'{self.get_walk_display()} on {self.date}' 
