from django import forms 
from appBD.models import Empleado,Cargo

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields='__all__'

class CargoForm(forms.ModelForm):
    class Meta:
        model=Cargo
        fields='__all__'