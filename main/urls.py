from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.main_view),
    path('get_jobs/', views.get_jobs, name='get_jobs'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
