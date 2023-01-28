from .models import *
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def hola(request):
    if request.method == "GET":
        return render(request, "index.html", {
            "form": Ingreso()
        })
    else:
        usuario = request.POST.get("username")
        contraseña = request.POST.get("password")
        # imprime de momento en consola que no se puede usar ese usuario
        for alum in Alumno.objects.all():
            if alum.username == usuario:
                mensaje = 'Usuario existe'
                print("\n" + mensaje + "\n")
                if alum.password == contraseña:
                    mensaje = 'Autenticación Exitosa'
                    print("\n" + mensaje + "\n")
                    return redirect("/horario/")
            else:
                mensaje = 'Usuario o contraseña incorrectas'
                print("\n" + mensaje + "\n")
                return redirect("/")


def registro(request):
    if request.method == "GET":
        return render(request, "registro.html", {
            "form": CreateStudent()
        })
    else:
        usuario = request.POST.get("username")
        if Alumno.objects.filter(username=usuario).count():
            # imprime de momento en consola que no se puede usar ese usuario
            mensaje = 'Usuario ya existe, utilice otro'
            print("\n" + mensaje + "\n")
            return redirect("/registro/")
        else:
            Alumno.objects.create(email=request.POST["email"], f_name=request.POST["f_name"],
                                  l_name=request.POST["l_name"], password=request.POST["password"],
                                  username=request.POST["username"])
            mensaje = 'Usuario creado con exito'
            print("\n" + mensaje + "\n")
            return redirect("/")


def horario(request):
    if request.method == "GET":
        return render(request, "horario.html", {
            "form": Materias()
        })
    else:
        Materia.objects.create(name=request.POST["name"], curso=request.POST["curso"],
                               horario=request.POST["horario"], profesor_id=int(request.POST["profesor"]),
                               alumno_id=int(request.POST["alumno"]))
        mensaje = 'Registro creado con exito'
        print("\n" + mensaje + "\n")
        return redirect("/")


def profesores(request):
    if request.method == "GET":
        return render(request, "profesores.html", {
            "form": Profesor()
        })
    else:
        usuario = request.POST.get("username")
        if Maestro.objects.filter(username=usuario).count():
            # imprime de momento en consola que no se puede usar ese usuario
            mensaje = 'Usuario ya existe, utilice otro'
            print("\n" + mensaje + "\n")
            return redirect("/profesores/")
        else:
            Maestro.objects.create(email=request.POST["email"], f_name=request.POST["f_name"],
                                  l_name=request.POST["l_name"], password=request.POST["password"],
                                  username=request.POST["username"])
            mensaje = 'Usuario creado con exito'
            print("\n" + mensaje + "\n")
            return redirect("/")