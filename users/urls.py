from django.urls import path
from users.views import UserCreateView, login_user, User_profile

urlpatterns =[
    path('singup/', UserCreateView.as_view(), name='singup'),
    path('login/', login_user, name='login'),
    path('profile/<int:id>', User_profile, name='profile'),
]