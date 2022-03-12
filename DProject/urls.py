
from django.contrib import admin
from django.urls import path, include
from DiProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('DiProject.urls_config'))
]

handler404 = PageNotFoundHandler
