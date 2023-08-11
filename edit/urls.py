from django.urls import path
from . import views

urlpatterns = [
    path('get_job_edit/', views.get_job_edit, name='get_job_edit'),
    path('', views.edit_job_suitability, name='edit_job_suitability'),
]
