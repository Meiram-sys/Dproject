from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='MainPage'),
    path('login/', LogUser.as_view(), name='Login'),
    path('accounts/profile/',LogUser.as_view(),name='Login'),
    path('register', RegUser.as_view(), name='Register'),
    path('add-article', AddArticle.as_view(), name='AddArticle'),
    path('search-resutl', SearchResultsView.as_view(), name='search_results'),
    path('logout',UserLogout,name='logout'),
    path('individuals', IndividualsAbout.as_view(), name='individuals'),
    path('category/<int:category_id>',show_category,name='category')

]
