from django.urls import path
from . import views

urlpatterns = [
    path('hola/<str:username>', views.hola),
    path('add/<int:id>', views.add),
    path('alumno/', views.alumno),
    #path('maestro/', views.maestro),
    #path('materia/', views.materia),
]