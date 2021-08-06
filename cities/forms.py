from django import forms
from django.db import models
from django.db.models import fields
from .models import City, University, CityImage, UniversityImage


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city', 'description', 'population']
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'population': forms.NumberInput(attrs={'class': 'form-control'})
        }


class CityImageForm(forms.ModelForm):
    class Meta:
        model = CityImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ['city', 'university', 'description', 'number_of_people']


class UniversityImageForm(forms.ModelForm):
    class Meta:
        model = UniversityImage
        fields = ['image', 'university']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
