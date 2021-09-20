from django.urls import path
from django.conf.urls import url
from users.views import *
from allauth.account.views import confirm_email


urlpatterns =[
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]