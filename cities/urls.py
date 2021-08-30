from django.urls import path
from .views import (
    IndexListView,
    city_detail,
    create_city,
    create_university,
    update_city,
    update_university,
    delete_city,
    university_delete,
    university_detail
)

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('city_detail/<int:id>/', city_detail, name='detail_city'),
    path('update_city/<int:id>/', update_city, name='update_city'),
    path('create_city/', create_city, name='create_city'),
    path('delete_city/<int:id>', delete_city, name='delete_city'),
    # path('all_universities', all_universities, name='all_universities'),
    path('university_detail/<int:id>/', university_detail ,name='university'),
    path('create_university/', create_university, name='create_university'),
    path('update_university/<int:id>', update_university, name='update_university'),
    path('delete_university/<int:id>', university_delete, name='delete_university'),
]
