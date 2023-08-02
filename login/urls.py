# urls.py
from django.urls import path
from .views import MyLoginView, MainView

urlpatterns = [
    path('', MyLoginView.as_view(), name='login'),
    path('main/', MainView.as_view(), name='main'),
   
]
