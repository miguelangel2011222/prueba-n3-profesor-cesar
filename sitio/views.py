from django.shortcuts import render,redirect
from sitio.forms import AlumnitoForm
import requests
from django.http import JsonResponse

API_URL ="http://127.0.0.1:8000/Alumnos-API-Clases/"
# Create your views here.

def Index_Alumnito(request):
    return render(request,"index.html")

def Create_Alumnito(request):
    form=AlumnitoForm()
    if request.method == "POST":
        # Obtener los datos enviados desde el formulario
        aluid=request.POST.get("id")
        rut = request.POST.get("ALUMRUT")
        nombre = request.POST.get("ALUMNOMBRE")
        apaterno = request.POST.get("ALUMAPATERNO")
        amaterno = request.POST.get("ALUMAMATERNO")
        direct = request.POST.get("ALUMDIRECCION")
        email = request.POST.get("ALUMEMAIL")
        fono = request.POST.get("ALUMFONO")

        # Crear el payload para la API
        payload = {
            "id":aluid,
            "ALUMRUT":rut,
            "ALUMNOMBRE": nombre,
            "ALUMAPATERNO": apaterno,
            "ALUMAMATERNO": amaterno,
            "ALUMDIRECCION": direct,
            "ALUMEMAIL": email,
            "ALUMFONO": fono,
        }
        # Llamar al método POST de la API REST
        response = requests.post(f"{API_URL}/", json=payload)

        # Manejar la respuesta de la API
        if response.status_code == 201:
            # Si se actualizó correctamente, redirigir o responder con éxito
             return render(request,"index.html")
        else:
            # Si hubo un error, devolver un mensaje de error
            return JsonResponse({"message": "Error al Crear el empleado"}, status=response.status_code)
    data={'form':form}
    return render(request,'create.html',data)

def View_Alumnito(request, id):
    api_url = f"{API_URL}/{id}"
    response = requests.get(api_url)
    Alumnazo = response.json() if response.status_code == 200 else None
    return render(request, 'view.html', {'Alumnazo':Alumnazo})