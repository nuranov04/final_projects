from django.shortcuts import render
from .models import Faculty
from django.db.models import Q


def all_faculty(request):
    faculty = Faculty.objects.all()
    return render(request, "all_faculties.html", {'faculties': faculty})

def faculty_detail(request, id):
    faculty_obj = Faculty.objects.get(id=id)
    return render(request, 'faculty_detail.html', locals())