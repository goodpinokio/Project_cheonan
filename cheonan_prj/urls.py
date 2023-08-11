from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('main.urls')),
    path('',include('login.urls')),
    path('table/',include('table.urls')),
    path('enroll/',include('enroll.urls')),
    path('edit/',include('edit.urls')),
]
