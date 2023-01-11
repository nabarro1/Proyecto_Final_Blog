from django.shortcuts import render, get_object_or_404
from appDjango.models import Familiar, Mascota, Vehiculo
from appDjango.forms import Buscar, FamiliarForm, MascotaForm, VehiculoForm,BuscarVehiculo # <--- NUEVO IMPORT
from django.views import View # <-- NUEVO IMPORT 
from django import forms
# Create your views here.


#------------------------------------FAMILIAR-----------------------------

def mostrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "appDjango/mi-familia.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'appDjango/buscarFamiliar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        msg_error = f"No se encontro el familiar"
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})
    
class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'appDjango/altaFamiliar.html'
    initial = {"nombre":"", "dni":"", "fecha_de_nacimiento":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})    



class ActualizarFamiliar(View):
  form_class = FamiliarForm
  template_name = 'appDjango/actualizarFamiliar.html'
  initial = {"nombre":"", "dni":"", "fecha_de_nacimiento":""}
  
  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(instance=familiar)
      return render(request, self.template_name, {'form':form,'familiar': familiar})

  def post(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      form = self.form_class(request.POST ,instance=familiar)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'familiar': familiar,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})
  
class BorrarFamiliar(View):
  template_name = 'appDjango/mi-familia.html'

  def get(self, request, pk): 
      familiar = get_object_or_404(Familiar, pk=pk)
      familiar.delete()
      familiares = Familiar.objects.all()
      return render(request, self.template_name, {'lista_familiares': familiares})

#------------------------------MASCOTA--------------------------------

def mostrar_mascotas(request):
  lista_mascotas = Mascota.objects.all()
  return render(request, "appDjango/mis-mascotas.html", {"lista_mascotas": lista_mascotas})

class AltaMascota(View):

    form_class = MascotaForm
    template_name = 'appDjango/altaMascota.html'
    initial = {"nombre":"", "edad":"", "animal":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito la mascota {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})    
    
class ActualizarMascota(View):
  form_class = MascotaForm
  template_name = 'appDjango/actualizarMascota.html'
  initial = {"nombre":"", "edad":"", "animal":""}
  
  def get(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(instance=mascota)
      return render(request, self.template_name, {'form':form,'mascota': mascota})

  def post(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      form = self.form_class(request.POST ,instance=mascota)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el familiar {form.cleaned_data.get('nombre')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'mascota': mascota,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})

class BorrarMascota(View):
  template_name = 'appDjango/mis-mascotas.html'

  def get(self, request, pk): 
      mascota = get_object_or_404(Mascota, pk=pk)
      mascota.delete()
      mascotas = Mascota.objects.all()
      return render(request, self.template_name, {'lista_mascotas': mascotas})


class BuscarMascota(View):
    form_class = Buscar
    template_name = 'appDjango/buscarMascota.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        msg_error = f"No se encontro la mascota"
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_mascotas = Mascota.objects.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_mascotas':lista_mascotas})
        return render(request, self.template_name, {"form": form})

#---------------------------- VEHICULO -----------------------------------------

def mostrar_vehiculos(request):
  lista_vehiculos = Vehiculo.objects.all()
  return render(request, "appDjango/vehiculos.html", {"lista_vehiculos": lista_vehiculos})

class BuscarVehiculo(View):
    form_class = BuscarVehiculo
    template_name = 'appDjango/buscarVehiculo.html'
    initial = {"marca":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        msg_error = f"No se encontro el Vehiculo"
        if form.is_valid():
            marca = form.cleaned_data.get("marca")
            lista_vehiculos = Vehiculo.objects.filter(marca__icontains=marca).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_vehiculos':lista_vehiculos})
        return render(request, self.template_name, {"form": form})
    
class AltaVehiculo(View):

    form_class = VehiculoForm
    template_name = 'appDjango/altaVehiculo.html'
    initial = {"tipo":"", "antiguedad":"", "marca":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el Vehiculo {form.cleaned_data.get('marca')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})   
    
class ActualizarVehiculo(View):
  form_class = VehiculoForm
  template_name = 'appDjango/actualizarVehiculo.html'
  initial = {"tipo":"", "antiguedad":"", "animal":""}
  
  def get(self, request, pk): 
      vehiculo = get_object_or_404(Vehiculo, pk=pk)
      form = self.form_class(instance=vehiculo)
      return render(request, self.template_name, {'form':form,'vehiculo': vehiculo})

  def post(self, request, pk): 
      vehiculo = get_object_or_404(Vehiculo, pk=pk)
      form = self.form_class(request.POST ,instance=vehiculo)
      if form.is_valid():
          form.save()
          msg_exito = f"se actualizó con éxito el Vehiculo {form.cleaned_data.get('marca')}"
          form = self.form_class(initial=self.initial)
          return render(request, self.template_name, {'form':form, 
                                                      'vehiculo': vehiculo,
                                                      'msg_exito': msg_exito})
      
      return render(request, self.template_name, {"form": form})
  
class BorrarVehiculo(View):
  template_name = 'appDjango/vehiculos.html'

  def get(self, request, pk): 
      vehiculo = get_object_or_404(Vehiculo, pk=pk)
      vehiculo.delete()
      vehiculos = Vehiculo.objects.all()
      return render(request, self.template_name, {'lista_vehiculos': vehiculos})