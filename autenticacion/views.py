from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import get_object_or_404, render
from .forms import CreateStudent
# Create your views here.
def hola(request):
    return render(request, "index.html")

def registro(request):
    if request.method == "GET":
        return render(request, "registro.html", {
            "form": CreateStudent()
        })
    else:
        Alumno.objects.create(username=request.GET["username"], f_name=request.GET["f_name"],
                              l_name=request.GET["l_name"], email=request.GET["email"],
                              password=request.GET["password"])


def horario(request):
    return render(request, "horario.html")
