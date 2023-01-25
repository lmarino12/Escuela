from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hola(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def chao(request):
    return HttpResponse("<h2>Chao</h2>")

def registro(request):
    alumnos = []
    alumno = []
    nombre = input("Ingrese su nombre: ")
    cedula = int(input("Ingrese su numero de cedula: "))
    edad = int(input("Ingrese su edad: "))
    celular = int(input("Ingrese su numero de telefono: "))
    correo = input("Ingrese su correo: ")
    alumno.append(nombre)
    alumno.append(cedula)
    alumno.append(edad)
    alumno.append(celular)
    alumno.append(correo)
    alumnos.append(alumno)
    alumno.clear()
    return HttpResponse(alumnos[0])