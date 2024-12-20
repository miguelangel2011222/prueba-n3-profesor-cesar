from django import forms 
from Prueba.models import Alumnos

class AlumnitoForm(forms.ModelForm):
    class Meta:
        model=Alumnos
        fields='__all__'