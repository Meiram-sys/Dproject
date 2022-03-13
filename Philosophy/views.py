from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from Philosophy.forms import *


class RegUser(CreateView):
    form_class = RegisterUser
    template_name = 'Philosophy/RegUser.html'
    success_url = reverse_lazy('MainPage')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class LogUser(LoginView):
    form_class = LoginUser
    template_name = 'Philosophy/LogUser.html'
    success_url = reverse_lazy('MainPage')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context


class MainPage(ListView):
    model = philosophers
    template_name = 'Philosophy/MainPage.html'
    context_object_name = 'philosophers'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class AddArticle(CreateView):
    form_class = AddArticle
    template_name = 'Philosophy/AddArticle.html'
    success_url = reverse_lazy('MainPage')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить статью'
        return context


def PageNotFoundHandler(request, exception):
    return HttpResponseNotFound('Page not found!')
