from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.
def hola(request, username):
    return HttpResponse("<h1>Hola %s</h1>" % username)

def add(request, id):
    # add = Task.objects.get(id=id)
    add = get_object_or_404(Task, id=id)
    return HttpResponse("Task %s" % add.title)

def alumno(request):
    alumno = list(Alumno.objects.values())
    return JsonResponse(alumno, safe=False)