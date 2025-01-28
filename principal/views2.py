from django.shortcuts import render, redirect
from principal.models import * 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseRedirect
from .forms import ActividadForm

# Vistas para login, perfil y home
def Login(request):

    return render(request, "login.html")

def Perfil(request):

    return render(request, "perfil.html")

def Home(request):

    return render(request, "index.html")

def Parametros2(request):
    
    return render(request, "Otros/index.html")

#Vista de el atajo para la tabla actividades 
def crear_actividad(request):
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La actividad se ha creado correctamente.')
            return redirect('principal2:leerProyectos')  
        else:
            messages.error(request, 'Hubo un error al crear la actividad.')
    else:
        form = ActividadForm()
    return render(request, 'crear_actividad.html', {'form': form})
#---------------------------Vista para Donaciones-----------------------------------#
class ListadoDonaciones(SuccessMessageMixin, CreateView, ListView):
    model = Donaciones
    fields = "__all__"
    queryset = Donaciones.objects.all()
    success_message = 'Donación creada satisfactoriamente'
    
    def get_success_url(self):        
        return reverse('principal2:leerDonaciones')

class DonacionesDetalle(DetailView):
    model = Donaciones

class DonacionesActualizar(SuccessMessageMixin, UpdateView):
    model = Donaciones
    fields = "__all__"
    success_message = 'Donación actualizada satisfactoriamente'
    
    def get_success_url(self):               
        return reverse('principal2:leerDonaciones')

class DonacionesEliminar(SuccessMessageMixin, DeleteView): 
    model = Donaciones
    
    def get_success_url(self): 
        success_message = 'Donación eliminada satisfactoriamente'
        messages.success(self.request, success_message)       
        return reverse('principal2:leerDonaciones')
#---------------------------Fin de Vistas para Donaciones--------------------------------#    

#---------------------------Vistas Para Notificaciones-----------------------------------#
class ListadoNotificaciones(SuccessMessageMixin, CreateView, ListView):
    model = Notificaciones
    fields = "__all__"
    queryset = Notificaciones.objects.all()
    success_message = 'Notificación creada satisfactoriamente'
    
    def get_success_url(self):        
        return reverse('principal2:leerNotificaciones')

class NotificacionesDetalle(DetailView):
    model = Notificaciones

class NotificacionesActualizar(SuccessMessageMixin, UpdateView):
    model = Notificaciones
    fields = "__all__"
    success_message = 'Notificación actualizada satisfactoriamente'
    
    def get_success_url(self):               
        return reverse('principal2:leerNotificaciones')

class NotificacionesEliminar(SuccessMessageMixin, DeleteView): 
    model = Notificaciones
    
    def get_success_url(self): 
        success_message = 'Notificación eliminada satisfactoriamente'
        messages.success(self.request, success_message)       
        return reverse('principal2:leerNotificaciones')
#---------------------------Fin de Vistas para Notificaciones-----------------------#

#---------------------------Vistas Para Proyectos-----------------------------------#
from .forms import ProyectosForm

class ListadoProyectos(SuccessMessageMixin, CreateView, ListView):
    model = Proyectos
    form_class = ProyectosForm  # Usar el formulario personalizado
    queryset = Proyectos.objects.all()
    success_message = 'Proyecto creado satisfactoriamente'

    def get_success_url(self):        
        return reverse('principal2:leerProyectos')

class ProyectosDetalle(DetailView):
    model = Proyectos

class ProyectosActualizar(SuccessMessageMixin, UpdateView):
    model = Proyectos
    form_class = ProyectosForm  # Usar el formulario personalizado
    success_message = 'Proyecto actualizado satisfactoriamente'

    def get_success_url(self):               
        return reverse('principal2:leerProyectos')

class ProyectosEliminar(SuccessMessageMixin, DeleteView): 
    model = Proyectos
    
    def get_success_url(self): 
        success_message = 'Proyecto eliminado satisfactoriamente'
        messages.success(self.request, success_message)       
        return reverse('principal2:leerProyectos')
#---------------------------Fin de Vistas para Proyectos---------------------------#    

#---------------------------Vistas para Recursos-----------------------------------#
class ListadoRecursos(SuccessMessageMixin, CreateView, ListView):
    model = Recursos
    fields = "__all__"
    queryset = Recursos.objects.all()
    success_message = 'Recurso creado satisfactoriamente'
    
    def get_success_url(self):        
        return reverse('principal2:leerRecursos')

class RecursosDetalle(DetailView):
    model = Recursos

class RecursosActualizar(SuccessMessageMixin, UpdateView):
    model = Recursos
    fields = "__all__"
    success_message = 'Recurso actualizado satisfactoriamente'
    
    def get_success_url(self):               
        return reverse('principal2:leerRecursos')

class RecursosEliminar(SuccessMessageMixin, DeleteView): 
    model = Recursos
    
    def get_success_url(self): 
        success_message = 'Recurso eliminado satisfactoriamente'
        messages.success(self.request, success_message)       
        return reverse('principal2:leerRecursos')
#---------------------------Fin de Vistas para Recursos-----------------------------------#    