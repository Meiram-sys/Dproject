
from django.contrib import admin
from django.urls import path, include
from Philosophy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Philosophy.urls_config'))
]

handler404 = PageNotFoundHandler
