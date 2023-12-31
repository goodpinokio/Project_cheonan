from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib import messages

class CustomLoginView(LoginView):
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, '비밀번호 또는 아이디가 틀렸습니다.')
        return response


class MyLoginView(LoginView):
    template_name = 'login/login.html'

    def get_success_url(self):
        return reverse('main')  # 로그인 성공 후 리다이렉트할 URL

class MainView(TemplateView):
    template_name = 'base_full_width.html'
