from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateStudent
from django import forms
# Create your views here.
def hola(request):
    return render(request, "index.html")

def registro(request):
    if request.method == "GET":
        return render(request, "registro.html", {
            "form": CreateStudent()
        })
    else:
        usuario=request.POST.get("username")
        if Alumno.objects.filter(username=usuario).count():
            #imprime de momento en consola que no se puede usar ese usuario
            mensaje = 'Usuario ya existe, utilice otro'
            print("\n"+mensaje+"\n")
            return redirect("/registro/")
        else:
            Alumno.objects.create(email=request.POST["email"], f_name=request.POST["f_name"],
                                l_name=request.POST["l_name"], password=request.POST["password"],
                                username=request.POST["username"])
            mensaje = 'Usuario creado con exito'
            print("\n" + mensaje + "\n")
            return redirect("/")

def horario(request):
    return render(request, "horario.html")
