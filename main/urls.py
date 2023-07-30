from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
