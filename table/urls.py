from django.urls import path
from . import views

urlpatterns = [
    path('table/', views.table_view,name='table_view'),  
]
