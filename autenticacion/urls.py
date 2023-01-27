from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola),
    path('registro/', views.registro),
    path('horario', views.horario),
]