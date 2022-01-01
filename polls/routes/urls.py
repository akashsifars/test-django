from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib import admin
from ..views import views, text, success, list

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', text.index, name='index'),
    path('submit/', success.index, name='index'),
    path('admin/', admin.site.urls),
    path('list/', list.list_data, name='list_data'), 
]