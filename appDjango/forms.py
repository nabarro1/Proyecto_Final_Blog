from django import forms
from appDjango.models import Familiar, Mascota, Vehiculo

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100)
    
class BuscarVehiculo(forms.Form):
    marca = forms.CharField(max_length=100)

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'dni', 'fecha_de_nacimiento']   
    
class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['nombre', 'edad', 'animal']   
    
class VehiculoForm(forms.ModelForm):
  class Meta:
    model = Vehiculo
    fields = ['tipo', 'antiguedad', 'marca']   
    