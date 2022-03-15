from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class RegisterUser(UserCreationForm):
    username = forms.CharField(label='Login',
                               widget=forms.TextInput(attrs={'class': 'username', 'placeholder': 'Логин'}))
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'class': 'email', 'placeholder': 'Ваш Емайл'}))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Ваш пароль'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(
        attrs={'class': 'password', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUser(AuthenticationForm):
    username = forms.CharField(label='Login',
                               widget=forms.TextInput(attrs={'class': 'username', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'password', 'placeholder': 'Пароль'}))


class AddArticle(forms.ModelForm):
    class Meta:
        model = philosophers
        fields = ['name', 'surname', 'philosophy_name', 'philosophy', 'birth_time', 'death_time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'name'}),
            'surname': forms.TextInput(attrs={'class': 'surname'}),
            'philosophy_name': forms.TextInput(attrs={'class': 'philosophy_name'}),
            'philosophy': forms.Textarea(attrs={'cols': 80, 'rows': 10, 'class': 'philosophy'}),
            'birth_time': forms.TextInput(attrs={'class': 'birth_time'}),
            'death_time': forms.TextInput(attrs={'class': 'death_time'})

        }


class SearchForm(forms.Form):
    query = forms.CharField()
