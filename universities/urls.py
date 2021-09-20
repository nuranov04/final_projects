from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


api_urlpatterns = [
    path('', include('cities.api.urls')),
    path('', include('fakultet.api.urls')),
]

urlpatterns = [
#       django rest
    path('api/', include(api_urlpatterns)),
    path('admin/', admin.site.urls),

    # local apps
    path('', include('cities.urls')),
    path("faculty/", include('fakultet.urls')),
    path('accounts/', include('users.urls')),
    url(r'^accounts/', include('allauth.urls'))
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
