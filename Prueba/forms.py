from django import forms 
from Prueba.models import Ciudades,Tipocurso,Alumnos,Usuarios, Sucursales



class CiudadesForm(forms.ModelForm):
    class Meta:
        model=Ciudades
        fields='__all__'

class TipoCursoForm(forms.ModelForm):
    class Meta:
        model=Tipocurso
        fields='__all__'

class AlumnosForm(forms.ModelForm):
    class Meta:
        model=Alumnos
        fields='__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model=Usuarios
        fields='__all__'


class MatriculaFilterForm(forms.Form):
    fecha_inicio = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    fecha_fin = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    sucursal = forms.ModelChoiceField(queryset=Sucursales.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))


        

