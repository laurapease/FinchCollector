from django import forms
from .models import Walking, Dog

class WalkingForm(forms.ModelForm):
  class Meta:
    model = Walking
    fields = ['date', 'note', 'walk']

class DogForm(forms.ModelForm):
  class Meta:
    model = Dog
    fields = ('name', 'breed', 'description', 'age')