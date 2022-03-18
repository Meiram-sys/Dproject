from django.contrib.auth import login, logout
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
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

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('MainPage')


class LogUser(LoginView):
    form_class = LoginUser
    template_name = 'Philosophy/LogUser.html'
    success_url = reverse_lazy('MainPage')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

def UserLogout(request):
    logout(request)
    return redirect('MainPage')

class AddArticle(CreateView):
    form_class = AddArticle
    template_name = 'Philosophy/AddArticle.html'
    success_url = reverse_lazy('MainPage')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить статью'
        return context


class SearchResultsView(ListView):
    model = philosophers
    template_name = 'Philosophy/MainPage.html'
    context_object_name = 'philosophy'

    def get_queryset(self):
        query = self.request.GET.get('search_q')
        result = philosophers.objects.filter(
            Q(name__icontains=query) | Q(surname__icontains=query) | Q(philosophy_name__icontains=query) | Q(
                philosophy__icontains=query))
        return result


class MainPage(ListView):
    model = philosophers
    template_name = 'Philosophy/MainPage.html'
    context_object_name = 'philosophy'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class IndividualsAbout(ListView):
    model = Individuals
    template_name = 'Philosophy/Individuals.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Личности'
        context['cat'] = category.objects.all()
        return context


def show_category(request, category_id):
    posts = Individuals.objects.filter(category_id=category_id)
    cat = category.objects.all()
    context = {
        'posts': posts,
        'cat': cat,
        'title': 'Category',
        'cat_selected': 0,
    }
    return render(request, 'Philosophy/Individuals.html', context=context)


def PageNotFoundHandler(request, exception):
    return HttpResponseNotFound('Page not found!')
