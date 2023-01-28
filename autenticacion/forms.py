from django import forms
from .models import *

class CreateStudent(forms.Form):
    username = forms.CharField(label="Usuario")
    f_name = forms.CharField(label="Primer Nombre")
    l_name = forms.CharField(label="Primer Apellido")
    email = forms.CharField(label="Correo")
    password = forms.CharField(label="Contraseña")

class Ingreso(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña")