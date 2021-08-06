from django.shortcuts import render, redirect
from .models import Faculty
from django.db.models import Q
from fakultet.forms import FacultyForm
from django.forms import inlineformset_factory


def all_faculty(request):
    faculty = Faculty.objects.all()
    if 'key_word' in request.GET:
        key = request.GET.get('words')
        faculty = Faculty.objects.filter(Q(faculty__icontains=key))
    else:
        faculty = Faculty.objects.all()
    return render(request, "faculties/all_faculties.html", {'faculties': faculty})


def faculty_detail(request, id):
    faculty_obj = Faculty.objects.get(id=id)
    return render(request, 'faculties/faculty_detail.html', locals())


def create_faculty(request):
    form = FacultyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('all_faculties')
    return render(request, 'faculties/create_faculty.html', locals())
