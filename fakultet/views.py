from django.db import models
from django.shortcuts import render, redirect
from .models import Faculty, Application
from django.core.mail import send_mail
from django.db.models import Q
from fakultet.forms import FacultyForm
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
    if 'application' in request.POST:
        email = request.POST.get('email')
        faculty = Faculty.objects.get(id=id)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        number_of_phone = request.POST.get('number_of_phone')
        application = Application.objects.create(email = email, faculty = faculty,
            first_name = first_name, last_name = last_name, number_of_phone = number_of_phone
        )
        message = f'Уважаемый {first_name} {last_name}, вы подали заявку на факультет "{faculty}". \n с Уважением сайт Артура)'
        print(message)
        send_mail(
            'Подача заявки на факультет',
            message,
            'nursultandev@gmail.com',
            [email],
            fail_silently=False
        )
        print('done')
        return redirect('index')
    return render(request, 'faculties/faculty_detail.html', {'faculty': faculty})


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



