from allauth.account.forms import LoginForm, SignupForm
from django import forms
from django.forms import fields, models


from users.models import User


class LoginForm(LoginForm):
    pass


class SingupForm(SignupForm):
    pass