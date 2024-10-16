from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthorizationView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorization.html'
    login_url = '/admin'

