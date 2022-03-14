from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='MainPage'),
    path('login', LogUser.as_view(), name='Login'),
    path('register', RegUser.as_view(), name='Register'),
    path('add-article',AddArticle.as_view(),name='AddArticle'),

]



