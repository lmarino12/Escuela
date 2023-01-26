from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hola(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def chao(request):
    return HttpResponse("<h2>Chao</h2>")
