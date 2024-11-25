from django.shortcuts import render,redirect,get_object_or_404
from Prueba.models import Ciudades,Tipocurso,Alumnos,Usuarios,Sucursales,Matriculas
from . import forms
from .forms import CiudadesForm,TipoCursoForm,AlumnosForm,UsuarioForm
from django.db.models import Q
# Create your views here.



#CIUDADES


def Index_Ciudades(request):
    query = request.GET.get('search')
    if query:
        ciudad = Ciudades.objects.filter(CIUNOMBRE__icontains=query)
    else:
        ciudad = Ciudades.objects.all()
    data = {'ciudad': ciudad}
    return render(request, 'ciudad.html', data)


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
    query = request.GET.get('search')
    if query:
        tipocursos = Tipocurso.objects.filter(TIPCURNOMBRE__icontains=query)
    else:
        tipocursos = Tipocurso.objects.all()
    data = {'tipocursos': tipocursos}
    return render(request, 'tipocurso.html', data)


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

def actualizar_tipoCurso(request, id):
    cursos=Tipocurso.objects.get(id=id)
    form=TipoCursoForm(instance=cursos)
    if request.method=="POST":
        form=TipoCursoForm(request.POST,instance=cursos)
        if form.is_valid():
            form.save()
        return Index_Tipo_Curso(request)
    data={'form':form,'titulo':'Actualizar Tipo Curso'}
    return render(request,'create-tipocurso.html',data)

def delete_tipoCurso(request, id):
    curso =Tipocurso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        return redirect("/tipo cursos/")
    data = {"curso": curso}
    return render(request, 'delete-tipoCurso.html', data)


#Alumos

def Index_Alumnos(request):
    alumno=Alumnos.objects.all() 
    data={'alumno':alumno}
    return render(request,'Alumno.html',data)

from django.db.models import Q

def Index_Alumnos_filtro2(request):
    query = Q()
    if 'rut' in request.GET and request.GET['rut']:
        query &= Q(ALUMRUT__icontains=request.GET['rut'])
    if 'nombre' in request.GET and request.GET['nombre']:
        query &= Q(ALUMNOMBRE__icontains=request.GET['nombre'])
    if 'apellido_paterno' in request.GET and request.GET['apellido_paterno']:
        query &= Q(ALUMAPATERNO__icontains=request.GET['apellido_paterno'])
    if 'apellido_materno' in request.GET and request.GET['apellido_materno']:
        query &= Q(ALUMAMATERNO__icontains=request.GET['apellido_materno'])

    alumno = Alumnos.objects.filter(query) 
    data = {'alumno': alumno}
    return render(request, 'AlumnoFiltro.html', data)

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

def actualizar_Alumno(request, id):
    alumno=Alumnos.objects.get(id=id)
    form=AlumnosForm(instance=alumno)
    if request.method=="POST":
        form=AlumnosForm(request.POST,instance=alumno)
        if form.is_valid():
            form.save()
        return Index_Alumnos(request)
    data={'form':form,'titulo':'Actualizar Datos alumnos'}
    return render(request,'create-alumnos.html',data)

def delete_Alumno(request, id):
    alumno =Alumnos.objects.get(id=id)
    if request.method == "POST":
        alumno.delete()
        return redirect("/alumnos/")
    data = {"alumno": alumno}
    return render(request, 'delete-alumno.html', data)


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

#Usuario

def Index_Usuario(request):
    query = request.GET.get('search')
    if query:
        usuario = Usuarios.objects.filter(USULOGIN__icontains=query)
    else:
        usuario = Usuarios.objects.all()
    data = {'usuario': usuario}
    return render(request, 'Usuario.html', data)



def View_Usuario(request,id):
    usuario=Usuarios.objects.get(id=id)
    data={"usuario":usuario}
    return render(request,'view-usuario.html',data)

def Update_Usuario(request,id):
    usuario=Usuarios.objects.get(id=id)
    form=UsuarioForm(instance=usuario)
    if request.method=="POST":
        form=UsuarioForm(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
        return Index_Usuario(request)
    data={'form':form,'titulo':'Actualizar usuario'}
    return render(request,'update-usuario.html',data)

#sucursales

def SucursalIndex(request):
    query = request.GET.get('search')
    if query:
        sucursal = Sucursales.objects.filter(SUCNOMBRE__icontains=query)
    else:
        sucursal = Sucursales.objects.all()
    data = {'sucursal': sucursal}
    return render(request, 'sucursales.html', data)

def sucursalCreate(request):
    sucursal=Sucursales()
    if request.method=='POST':
        sucursal.SUCNOMBRE=request.POST['txtsucursal']
        sucursal.SUCCODIGO=request.POST['txtsucursalcod']
        ciudad=Ciudades.objects.get(id=request.POST["ciudad"])
        sucursal.CIUCODIGO=ciudad
        sucursal.save()
        return SucursalIndex(request)
    else:
        ciudades=Ciudades.objects.all()
        data={'ciudades':ciudades}
        return render(request,'create-sucursal.html',data)
    
def sucursalView(request, id):
    sucursal = Sucursales.objects.get(id=id)
    data = {'sucursal': sucursal}
    return render(request, 'view-sucursal.html', data)

def sucursalUpdate(request, id):
    sucursal = get_object_or_404(Sucursales, id=id)
    if request.method == 'POST':
        sucursal.SUCNOMBRE=request.POST['txtsucursal']
        sucursal.SUCCODIGO=request.POST['txtsucursalcod']
        ciudad = Ciudades.objects.get(id=request.POST["ciudad"])
        sucursal.CIUCODIGO = ciudad
        sucursal.save()
        return redirect('/sucursal/')  

    else:
        ciudades = Ciudades.objects.all()
        data = {'sucursales':sucursal, 'ciudades': ciudades}
        return render(request, 'create-sucursal.html', data)


def sucursalDelete(request, id):
    sucursal = get_object_or_404(Sucursales, id=id)
    if request.method == 'POST':
        sucursal.delete()
        return redirect('/sucursal/')
    return render(request, 'delete-sucursal.html', {'sucursal': sucursal})




#matricula

def matriculaIndex(request):
    matriculas = Matriculas.objects.all()
    total_valor = sum(matricula.TIPCURCODIGO.TIPCURVALOR for matricula in matriculas)
    data = {
        'matriculas': matriculas,
        'total_valor': total_valor
    }
    return render(request, 'Matricula.html', data)


def matriculaIndexFiltro(request):
    sucursal_nombre = request.GET.get('sucursal', '')
    if sucursal_nombre:
        matriculas = Matriculas.objects.filter(SUCCODIGO__SUCNOMBRE__icontains=sucursal_nombre)
    else:
        matriculas = Matriculas.objects.all()
    total_valor = sum(matricula.TIPCURCODIGO.TIPCURVALOR for matricula in matriculas)
    data = {
        'matriculas': matriculas,
        'total_valor': total_valor,
        'sucursal_nombre': sucursal_nombre,
    }
    return render(request, 'MatriculaFiltro.html', data)




def matriculaCreate(request):
    if request.method == 'POST':
        matricula = Matriculas()
        matricula.MATNUMERO = request.POST['txtmatricula']
        matricula.MATFECHA = request.POST['xtmatricula1']
        tipcurso = Tipocurso.objects.get(id=request.POST["tipcurso"])
        matricula.TIPCURCODIGO = tipcurso
        rut = Alumnos.objects.get(id=request.POST["rut"])
        matricula.ALUMRUT = rut
        sucodigo = Sucursales.objects.get(id=request.POST["sucodigo"])
        matricula.SUCCODIGO = sucodigo
        matricula.save()
        return matriculaIndex(request)

    else:
        tipcursos = Tipocurso.objects.all()
        ruts = Alumnos.objects.all()
        sucodigos = Sucursales.objects.all()
        data = {
            'tipcursos': tipcursos,
            'ruts': ruts,
            'sucodigos': sucodigos
        }
        return render(request, 'create-matricula.html', data)

def matriculaView(request, id):
    matricula = Matriculas.objects.get(id=id)
    data = {'matricula': matricula}
    return render(request, 'view-matricula.html', data)

def matriculaUpdate(request, id):
    matricula = get_object_or_404(Matriculas, id=id)
    if request.method == 'POST':
        matricula.MATNUMERO = request.POST['txtmatricula']
        matricula.MATFECHA = request.POST['xtmatricula1']
        tipcurso = Tipocurso.objects.get(id=request.POST["tipcurso"])
        matricula.TIPCURCODIGO = tipcurso
        rut = Alumnos.objects.get(id=request.POST["rut"])
        matricula.ALUMRUT = rut
        sucodigo = Sucursales.objects.get(id=request.POST["sucodigo"])
        matricula.SUCCODIGO = sucodigo
        matricula.save()
        return redirect('/matriculas/')  

    else:
        tipcursos = Tipocurso.objects.all()
        ruts = Alumnos.objects.all()
        sucodigos = Sucursales.objects.all()
        data = {
            'matricula': matricula,
            'tipcursos': tipcursos,
            'ruts': ruts,
            'sucodigos': sucodigos
        }
        return render(request, 'create-matricula.html', data)
    

def matriculaDelete(request, id):
    matricula = get_object_or_404(Matriculas, id=id)
    if request.method == 'POST':
        matricula.delete()
        return redirect('/matriculas/')
    return render(request, 'delete-matricula.html', {'matricula': matricula})


