from django import forms
from django.db import models
from django.db.models import fields
from .models import City, University,CityImage



class CityForm(forms.ModelForm):
    
    class Meta:
        model=City
        fields=['city','description','population']
        exclude=['slug']
        widgets={
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'population':forms.NumberInput(attrs={'class':'form-control'})
        }

class CityImageForm(forms.ModelForm):


    class Meta:
        model=CityImage
        fields=['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
