from django import forms
from .models import Car

class CarsForm(forms.ModelForm):
    class Meta:
        model = Car
        fields="__all__"