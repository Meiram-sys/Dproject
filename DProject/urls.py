from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Philosophy.views import *

urlpatterns = [
    path('',include('Philosophy.urls_config'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = PageNotFoundHandler
