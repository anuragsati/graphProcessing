from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clearGraph', views.clearGraph, name='clearGraph'),
]
