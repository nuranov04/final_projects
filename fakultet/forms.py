from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from fakultet.models import Faculty, Application


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['university', 'faculty', 'description', 'price', 'open_or_close']


