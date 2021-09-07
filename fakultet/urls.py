from django.urls import path
from fakultet.views import (
    faculty_detail,
    create_faculty, 
    delete_faculty, 
    update_faculty, 
    ApplicationCreateView, 
    )


urlpatterns = [
    # path('all_faculties/', all_faculty, name='all_faculties'),
    path('faculty_detail/<int:id>', faculty_detail, name='faculty_detail'),
    path('create_faculty/', create_faculty, name='create_faculty'),
    path('update_faculty/<int:id>', update_faculty, name='update_faculty'),
    path('delete_faculty/<int:id>/', delete_faculty, name='delete_faculty'),
    path('application/', ApplicationCreateView.as_view(), name='application'),
]
