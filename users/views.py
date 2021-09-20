from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
from allauth.account.views import (
    LoginView, SignupView
)
from users.models import User
from users.forms import SingupForm, LoginForm


class SignupView(SignupView):
    template_name = 'singup.html'
    form_class = SingupForm
    redirect_field_name = 'account_email_verification_sent'


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    redirect_field_name = 'next'



