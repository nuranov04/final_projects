from django import forms
from django.db import models
from django.db.models import fields
from fakultet.models import Faculty


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['university', 'faculty', 'description', 'price']
