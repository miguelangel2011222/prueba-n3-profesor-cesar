"""
URL configuration for ProyectoBD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appBD.views import Index_Empleado,Create_Empleado,View_Empleado,Delete_Empleado,ComunaIndex,ComunaCreate,Update_Empleado


from Prueba.views import Index_Ciudades,Create_Ciudad,View_Ciudad,Delete_Ciudad,Update_Ciudad

from Prueba.views import Index_Tipo_Curso,Create_tipocurso,View_tipocurso

from Prueba.views import Index_Alumnos,Create_Alumno,View_Alumno

from Prueba.views import login_view

from Prueba.views import Index_Usuario,View_Usuario,Update_Usuario

urlpatterns = [
    #appbd
    path('admin/', admin.site.urls),
    path('empleados/',Index_Empleado),
    path('create-empleado/',Create_Empleado),
    path('view-empleado/<int:id>',View_Empleado),
    path('update-empleado/<int:id>',Update_Empleado),
    path('delete-empleado/<int:id>',Delete_Empleado),
    path('comuna-index/',ComunaIndex),
    path('create-comuna/',ComunaCreate),

    #Prueba

    #ciudad
    path('ciudades/',Index_Ciudades),
    path('ingresar-ciudades/',Create_Ciudad),
    path('view-ciudades/<int:id>',View_Ciudad),
    path('delete-ciudad/<int:id>',Delete_Ciudad),
    path('actualizar-ciudad/<int:id>',Update_Ciudad),

    #Tipo Curso
    path('tipo cursos/',Index_Tipo_Curso),
    path('ingresar-tipos de curso/',Create_tipocurso),
    path('view-tipo curso/<int:id>',View_tipocurso),

    #Alumnos
    path('alumnos/',Index_Alumnos),
    path('ingresar-alumnos/',Create_Alumno),
    path('view-alumnos/<int:id>',View_Alumno),


    #login
    path('login/',login_view,name='login'),


    #sucursales


    #matriculas


    #Usuarios
    path('usuario/',Index_Usuario),
    path('view-usuario/<int:id>',View_Usuario),
    path('actualizar-usuario/<int:id>',Update_Usuario),
]