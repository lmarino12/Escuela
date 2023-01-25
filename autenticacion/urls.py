from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola),
    path('chao/', views.chao),
    path('registro/', views.registro),
]