from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class RegisterUser(UserCreationForm):
    username = forms.CharField(label='Login')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Repeat password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUser(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
