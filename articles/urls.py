from django.contrib import admin
from django.urls import path

from . import views

# give the app a name to use
app_name = 'articles'

# urls and the functions in case of the url machtes
urlpatterns = [
    path('', views.articles_list, name='list'),
    path('<str:slug>', views.article_detail, name='detail'),
]
