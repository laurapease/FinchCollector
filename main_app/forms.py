from django import forms
from .models import Walking

class WalkingForm(forms.ModelForm):
  class Meta:
    model = Walking
    fields = ['date', 'note', 'walk']