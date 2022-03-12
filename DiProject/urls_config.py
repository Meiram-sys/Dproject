from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage, name='MainPage'),
    path('login', LogUser.as_view(), name='Login'),
    path('register', RegUser.as_view(), name='Register')
]



