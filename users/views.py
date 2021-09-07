from users.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from users.forms import UserCreateForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages


class UserCreateView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = "singup.html"


def login_user(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        except:
            messages.error(request, 'Not correct login or password')
    return render(request, 'login.html')

def User_profile(request, id):
    profile = User.objects.get(id=id)
    return render(request, 'profile.html', locals())
