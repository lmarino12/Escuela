from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hola(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def chao(request):
    return HttpResponse("<h2>Chao</h2>")

def registro(request):
    alumnos = []
    nombre = input("Ingrese su nombre: ")
    cedula = int(input("Ingrese su numero de cedula: "))
    edad = int(input("Ingrese su edad: "))
    celular = int(input("Ingrese su numero de telefono: "))
    correo = input("Ingrese su correo: ")