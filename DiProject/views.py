from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from DiProject.forms import *


class RegUser(CreateView):
    form_class = RegisterUser
    template_name = 'DiProject/RegUser.html'
    success_url = reverse_lazy('MainPage')


class LogUser(LoginView):
    form_class = LoginUser
    template_name = 'DiProject/LogUser.html'
    success_url = reverse_lazy('MainPage')


def MainPage(request):
    return render(request, 'DiProject/MainPage.html')


def PageNotFoundHandler(request, exception):
    return HttpResponseNotFound('Page not found!')
