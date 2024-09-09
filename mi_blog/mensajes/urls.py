"""
Este archivo define las rutas principales del proyecto mi_blog.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
