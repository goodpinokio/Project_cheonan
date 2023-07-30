from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView


class MyLoginView(LoginView):
    template_name = 'login/login.html'

    def get_success_url(self):
        return reverse('main')  # 로그인 성공 후 리다이렉트할 URL

class MainView(TemplateView):
    template_name = 'base_full_width.html'
