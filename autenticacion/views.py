from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import get_object_or_404, render
# Create your views here.
def hola(request):
    return render(request, "index.html")

def registro(request):
    #materia = list(Materia.objects.values())
    materias = Materia.objects.all()
    return render(request, "registro.html", {
        "materias": materias
    })

def horario(request):
    return render(request, "horario.html")