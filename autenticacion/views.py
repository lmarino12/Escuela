from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import get_object_or_404, render
# Create your views here.
def hola(request):
    return render(request, "index.html")

def registro(request):
    return render(request, "registro.html")

def horario(request):
    return render(request, "horario.html")