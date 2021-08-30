from django.urls import path
from users.views import UserCreateView, login_user

urlpatterns =[
    path('singup/', UserCreateView.as_view(), name='singup'),
    path('login/', login_user, name='login')
]