from django.db import models
from django.shortcuts import render, redirect
from .models import University, City, CityImage
from fakultet.models import Faculty
from django.views import generic
from django.db.models import Q
from cities.forms import CityForm


def index(request):
    university = University.objects.all()
    faculty = Faculty.objects.all()
    cities = City.objects.all()

    if 'key_word' in request.GET:
        key = request.GET.get('words')
        posts = City.objects.filter(Q(city=key) | Q(description=key))
    else:
        posts = City.objects.all()
    return render(request, 'index.html', {'university': university, 'faculty': faculty, 'cities': cities, })


def city_detail(request, id):
    city_obj = City.objects.get(id=id)
    return render(request, 'city_detail.html', {'city': city_obj})


def create_city(request):
    form = CityForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'create_city.html', locals())


def all_universities(request):
    university = University.objects.all()
    return render(request, 'all_universities.html', {'universities': university})


def university_detail(request, id):
    university = University.objects.get(id=id)
    return render(request, 'university_detail.html', {'university': university})
