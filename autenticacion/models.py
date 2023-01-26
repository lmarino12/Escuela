from django.db import models

# Create your models here.

class Alumno(models.Model):
    name = models.CharField(max_length=200)
    cedula = models.IntegerField(max_length=10)
    telf = models.IntegerField(max_length=10)
    correo = models.CharField(max_length=200)

class Maestro(models.Model):
    name = models.CharField(max_length=200)
    cedula = models.IntegerField(max_length=10)
    telf = models.IntegerField(max_length=10)
    correo = models.CharField(max_length=200)

class Materia(models.Model):
    name = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)
    horario = models.CharField(max_length=200)
    profesor = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)