from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class Alumno(models.Model):
    name = models.CharField(max_length=200)
    cedula = models.IntegerField()
    telf = models.IntegerField()
    correo = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Maestro(models.Model):
    name = models.CharField(max_length=200)
    cedula = models.IntegerField()
    telf = models.IntegerField()
    correo = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class CustomUser(UserCreationForm):
    class Alumno_:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]

class Materia(models.Model):
    name = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)
    horario = models.CharField(max_length=200)
    profesor = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    def __str__(self):
        return self.name, self.alumno.name, self.profesor.name