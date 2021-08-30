from django.db import models
from django.shortcuts import render, redirect
from .models import Faculty, Application
from django.db.models import Q
from fakultet.forms import FacultyForm, ApplicationForm
from django.views.generic import CreateView


# def all_faculty(request):
#     faculty = Faculty.objects.all()
#     if 'key_word' in request.GET:
#         key = request.GET.get('words')
#         faculty = Faculty.objects.filter(Q(faculty__icontains=key))
#     else:
#         faculty = Faculty.objects.all()
#     return render(request, "faculties/all_faculties.html", {'faculties': faculty})


def faculty_detail(request, id):
    faculty = Faculty.objects.get(id=id)
    return render(request, 'faculties/faculty_detail.html', locals())


def create_faculty(request):
    form = FacultyForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'faculties/create_faculty.html', locals())\



def delete_faculty(request, id):
    faculty_obj = Faculty.objects.get(id=id)
    if request.method == "POST":
        faculty_obj.delete()
        return redirect('index')
    return render(request, 'faculties/delete.html', locals())


def update_faculty(request, id):
    faculty_obj = Faculty.objects.get(id=id)
    form = FacultyForm(request.POST or None,  instance=faculty_obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save
            return redirect('index')
    return render(request, 'faculties/update.html', locals())


class ApplicationCreateView(CreateView):
    model = Application
    form_class = ApplicationForm
    success_url = '/'
    template_name = 'faculties/create_faculty.html'

    def form_valid(self, form):
        if form.instance:
            if form.open_or_close == 'True':
                form.save()
        return super().form_valid(form)