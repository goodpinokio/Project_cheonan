from django.urls import path
from . import views

urlpatterns = [
    path('', views.table_view,name='table_view'),  
]
