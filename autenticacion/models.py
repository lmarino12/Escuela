from django.db import models
# Create your models here.

class Alumno(models.Model):
    username = models.CharField(max_length=200)
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class Maestro(models.Model):
    username = models.CharField(max_length=200)
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Materia(models.Model):
    name = models.CharField(max_length=200)
    curso = models.CharField(max_length=200)
    horario = models.CharField(max_length=200)
    profesor = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    def __str__(self):
        return self.name, self.alumno.username, self.profesor.username