from django.shortcuts import render,redirect
from Prueba.models import Ciudades,Tipocurso,Alumnos,Usuarios
from . import forms
from .forms import CiudadesForm,TipoCursoForm,AlumnosForm
# Create your views here.



#CIUDADES

def Index_Ciudades(request):
    ciudad=Ciudades.objects.all() 
    data={'ciudad':ciudad}
    return render(request,'ciudad.html',data)

def Create_Ciudad(request):
    form=CiudadesForm()
    if request.method=='POST':
        form=CiudadesForm(request.POST)
        if form.is_valid():
            form.save()
        return Index_Ciudades(request)
    data={'form':form,'titulo':'Agregar Ciudad'}
    return render(request,'create-ciudad.html',data)

def View_Ciudad(request,id):
    ciudad=Ciudades.objects.get(id=id)
    data={"ciudad":ciudad}
    return render(request,'view-ciudad.html',data)

def Delete_Ciudad(request, id):
    ciudad =Ciudades.objects.get(id=id)
    if request.method == "POST":
        ciudad.delete()
        return redirect("/ciudades")
    data = {"ciudad": ciudad}
    return render(request, 'delete-ciudad.html', data)

def Update_Ciudad(request,id):
    ciudad=Ciudades.objects.get(id=id)
    form=CiudadesForm(instance=ciudad)
    if request.method=="POST":
        form=CiudadesForm(request.POST,instance=ciudad)
        if form.is_valid():
            form.save()
        return Index_Ciudades(request)
    data={'form':form,'titulo':'Actualizar ciudad'}
    return render(request,'create-ciudad.html',data)


#Tipo de Curso

def Index_Tipo_Curso(request):
    tipocursos=Tipocurso.objects.all() 
    data={'tipocursos':tipocursos}
    return render(request,'tipocurso.html',data)

def Create_tipocurso(request):
    form=TipoCursoForm()
    if request.method=='POST':
        form=TipoCursoForm(request.POST)
        if form.is_valid():
            form.save()
        return Index_Tipo_Curso(request)
    data={'form':form,'titulo':'Agregar un tipo de curso'}
    return render(request,'create-tipocurso.html',data)

def View_tipocurso(request,id):
    tipocursos=Tipocurso.objects.get(id=id)
    data={"tipocursos":tipocursos}
    return render(request,'view-tipocurso.html',data)


#Alumos

def Index_Alumnos(request):
    alumno=Alumnos.objects.all() 
    data={'alumno':alumno}
    return render(request,'Alumno.html',data)

def Create_Alumno(request):
    form=AlumnosForm()
    if request.method=='POST':
        form=AlumnosForm(request.POST)
        if form.is_valid():
            form.save()
        return Index_Alumnos(request)
    data={'form':form,'titulo':'Agregar un tipo de alumno'}
    return render(request,'create-alumnos.html',data)

def View_Alumno(request,id):
    alumno=Alumnos.objects.get(id=id)
    data={"alumno":alumno}
    return render(request,'view-alumno.html',data)


#login

def login_view(request):
    if request.method == "POST":
        usulogin = request.POST['usulogin']
        usupassword = request.POST['usupassword']
        try:
            usuario = Usuarios.objects.get(USULOGIN=usulogin, USUPASSWORD=usupassword)
            return render(request, 'ciudad.html')  # Redirige a una página de éxito
        except Usuarios.DoesNotExist:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

