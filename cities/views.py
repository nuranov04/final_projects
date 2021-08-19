from typing import Any
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .models import University, City, CityImage, UniversityImage
from fakultet.models import Faculty
from django.db.models import Q
from cities.forms import CityForm, CityImageForm, UniversityForm, UniversityImageForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView


# def index(request):
#     university = University.objects.all()
#     faculty = Faculty.objects.all()
#     page = request.GET.get('page', 1)
#     paginator = Paginator(faculty, 4)
#     cities = City.objects.all()
#     try:
#         faculties = paginator.page(page)
#     except PageNotAnInteger:
#         faculties = paginator.page(1)
#     except EmptyPage:
#         faculties = paginator.page(paginator.num_pages)
#     if 'key_word' in request.GET:
#         key = request.GET.get('words')
#         cities = City.objects.filter(Q(city__icontains=key))
#     else:
#         cities = City.objects.all()
#     return render(request, 'main.html', locals())


class IndexListView(ListView):
    template_name = 'main.html'
    context_object_name = 'cities'

    def get_queryset(self):
        return City.objects.all()

    def get_context_data(self, **kwargs: Any):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['university'] = University.objects.all()
        context['faculty'] = Faculty.objects.all()
        return context

# CRUD FOR CITIES

def city_detail(request, id):
    city_obj = City.objects.get(id=id)
    return render(request, 'single.html', {'city': city_obj})


def update_city(request, id):
    city = get_object_or_404(City, id=id)
    form = CityForm(request.POST, None, instance=city)
    CityImageFormset = inlineformset_factory(
        City, CityImage, form=CityImageForm, extra=1)
    if form.is_valid():
        city = form.save()
        formset = CityImageFormset(request.POST, request.FILES, instance=city)
        if formset.is_valid():
            formset.save()
        return redirect('index')
    formset = CityImageFormset(instance=city)
    return render(request, 'cities/update_city.html', locals())


def delete_city(request, id):
    city_obj = City.objects.get(id=id)
    if request.method == "POST":
        city_obj.delete()
        return redirect('index')
    return render(request, 'cities/delete.html', locals())


def create_city(request):
    form = CityForm(request.POST or None)
    CityImageFormset = inlineformset_factory(
        City, CityImage, form=CityImageForm, extra=1)
    if form.is_valid():
        city = form.save()
        formset = CityImageFormset(request.POST, request.FILES, instance=city)
        if formset.is_valid():
            formset.save()
        return redirect('index')
    formset = CityImageFormset()
    return render(request, 'cities/create_city.html', locals())


# CRUD FOR UNIVERSITIES
def all_universities(request):
    university = University.objects.all()
    if 'key_word' in request.GET:
        key = request.GET.get('words')
        university = University.objects.filter(Q(university__icontains=key))
    else:
        university = University.objects.all()
    return render(request, 'universities/all_universities.html', {'universities': university})


def create_university(request):
    form = UniversityForm(request.POST or None)
    UniversityImageFormset = inlineformset_factory(
        University, UniversityImage, form=UniversityImageForm, extra=1)
    if form.is_valid():
        university = form.save()
        formset = UniversityImageFormset(
            request.POST, request.FILES, instance=university)
        if formset.is_valid():
            formset.save()
        return redirect('all_universities')
    formset = UniversityImageFormset()
    return render(request, 'universities/create_university.html', locals())


def update_university(request, id):
    university = University.objects.get(id=id)
    form = UniversityForm(request.POST or None, instance=university)
    UniversityImageFormset = inlineformset_factory(
        University, UniversityImage, form=UniversityImageForm, extra=1)
    if form.is_valid():
        university = form.save()
        formset = UniversityImageFormset(
            request.POST, request.FILES, instance=university)
        if formset.is_valid():
            formset.save()
        return redirect('index')
    formset = UniversityImageFormset()
    return render(request, 'universities/update_university.html', locals())


def university_delete(request, id):
    university_obj = University.objects.get(id=id)
    if request.method == "POST":
        university_obj.delete()
        return redirect('all_universities')
    return render(request, 'universities/delete.html', locals())


def university_detail(request, id):
    faculties = Faculty.objects.all()
    university = University.objects.get(id=id)
    return render(request, 'universities/single.html', locals())


# class UniversityDetail(DetailView):
    # queryset = Faculty.objects.all()
    # model = Faculty
    # template_name = 'universities/detail.html'
    # context_object_name = 'faculties'

    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['university'] = University.objects.all()
        # return context
