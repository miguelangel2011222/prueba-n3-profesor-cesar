from django.shortcuts import render,redirect
from appBD.models import Empleado,Ciudad,Comuna
from . import forms
from .forms import EmpleadoForm
# Create your views here.

## Tabla:Empleados #####
def Index_Empleado(request):
    empleados=Empleado.objects.all() #Select * from empleados
    data={'empleados':empleados}
    return render(request,'empleados.html',data)

def Create_Empleado(request):
    form=EmpleadoForm()
    if request.method=='POST':
        form=EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
        return Index_Empleado(request)
    data={'form':form,'titulo':'Agregar Empleado'}
    return render(request,'create-empleado.html',data)

def View_Empleado(request,id):
    empleado=Empleado.objects.get(id=id)
    data={"empleado":empleado}
    return render(request,'view-empleado.html',data)

def Update_Empleado(request,id):
    empleado=Empleado.objects.get(id=id)
    form=EmpleadoForm(instance=empleado)
    if request.method=="POST":
        form=EmpleadoForm(request.POST,instance=empleado)
        if form.is_valid():
            form.save()
        return Index_Empleado(request)
    data={'form':form,'titulo':'Actualizar Empleado'}
    return render(request,'create-empleado.html',data)


def Delete_Empleado(request,id):
    empleado=Empleado.objects.get(id=id)
    empleado.delete()
    return redirect("/empleados")

##Fin Tabla Empleados

## Tabla Cargos  ###


## Fin Tabla Cargos ###

#Tabla: Comuna 
def ComunaIndex(request):
    comunas=Comuna.objects.all()
    data={'comunas':comunas}
    return render(request,'comuna-index.html',data)

def ComunaCreate(request):
    comuna=Comuna()
    if request.method=='POST':
        comuna.nombre=request.POST['txtcomuna']
        ciudad=Ciudad.objects.get(id=request.POST["ciudad"])
        comuna.ciudad=ciudad
        comuna.save()
        return ComunaIndex(request)
    else:
        ciudades=Ciudad.objects.all()
        data={'ciudades':ciudades}
        return render(request,'create-comuna.html',data)
    
    
def ComunaView(request,id):
    comuna=Comuna.object.get(id=id)
    data={'comuna':comuna}
    return render(request,'comuna-view.html',data)

#Fin Tabla: Comuna  
    
    