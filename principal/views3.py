from django.shortcuts import render, redirect
from principal.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseRedirect
from .forms import SignUpForm
from.forms import RegionForm
# Vistas para login, perfil y home
def Login(request):

    return render(request, "login.html")

def Perfil(request):

    return render(request, "perfil.html")

def Home(request):

    return render(request, "index.html")

def Parametros3(request):
    
    return render(request, "Listados/index.html")

# Vista para el registro de usuario
class SignUpView(CreateView):
    model = AuthUser
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('login')
    
# Vista de el atajo para la tabla seguimientos 
def crear_region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La region se ha creado correctamente.')
            return redirect("principal3:leerSeguimientos")  
        else:
            messages.error(request, 'Hubo un error al crear la region.')
    else:
        form = RegionForm()
    return render(request, 'crear_region.html', {'form': form})

#---------------------------Vistas para Regiones-----------------------------------#
class ListadoRegiones(SuccessMessageMixin, CreateView, ListView):
    model = Regiones
    fields = "__all__"
    queryset = Regiones.objects.all()
    success_message = 'Región creada satisfactoriamente'
    
    def get_success_url(self):        
        return reverse('principal3:leerRegiones')

class RegionesDetalle(DetailView):
    model = Regiones

class RegionesActualizar(SuccessMessageMixin, UpdateView):
    model = Regiones
    fields = "__all__"
    success_message = 'Región actualizada satisfactoriamente'
    
    def get_success_url(self):               
        return reverse('principal3:leerRegiones')

class RegionesEliminar(SuccessMessageMixin, DeleteView): 
    model = Regiones
    
    def get_success_url(self): 
        success_message = 'Región eliminada satisfactoriamente'
        messages.success(self.request, success_message)       
        return reverse('principal3:leerRegiones')
#---------------------------Fin de Vistas para Regiones--------------------------------#

#---------------------------Vistas para Seguimientos-----------------------------------#
class ListadoSeguimientos(SuccessMessageMixin, CreateView, ListView):
    model = Seguimientos
    fields = "__all__"
    queryset = Seguimientos.objects.all()
    success_message = 'Seguimiento creado satisfactoriamente'
    
    def get_success_url(self):        
        return reverse('principal3:leerSeguimientos')

class SeguimientosDetalle(DetailView):
    model = Seguimientos

class SeguimientosActualizar(SuccessMessageMixin, UpdateView):
    model = Seguimientos
    fields = "__all__"
    success_message = 'Seguimiento actualizado satisfactoriamente'
    
    def get_success_url(self):               
        return reverse('principal3:leerSeguimientos')

class SeguimientosEliminar(SuccessMessageMixin, DeleteView): 
    model = Seguimientos
    
    def get_success_url(self): 
        success_message = 'Seguimiento eliminado satisfactoriamente'
        messages.success(self.request, success_message)       
        return reverse('principal3:leerSeguimientos')
#---------------------------Fin de Vistas para Seguimientos---------------------#

#---------------------------Vistas para Proyectos_Actividades-----------------------------------#
from .forms import ProyectosForm

class ListadoProyectosActividades(SuccessMessageMixin, CreateView, ListView):
    model = ProyectosActividades
    form_class = ProyectosForm  # Usar el formulario personalizado
    queryset = ProyectosActividades.objects.all()
    success_message = 'Listado creado satisfactoriamente'
    
    def get_success_url(self):        
        return reverse('principal3:leerProyectosActividades')

class ProyectosActividadesActualizar(SuccessMessageMixin, UpdateView):
    model = ProyectosActividades
    form_class = ProyectosForm  # Usar el formulario personalizado
    success_message = 'Listado actualizado satisfactoriamente'
    
    def get_success_url(self):               
        return reverse('principal3:leerProyectosActividades')

class ProyectosActividadesEliminar(SuccessMessageMixin, DeleteView): 
    model = ProyectosActividades
    
    def get_success_url(self): 
        success_message = 'Listado eliminado satisfactoriamente'
        messages.success(self.request, success_message)       
        return reverse('principal3:leerProyectosActividades')
#---------------------------Fin de Vistas para Proyectos_Actividades--------------------------------------------#

#---------------------------Vistas para Sesiones de Formacion-----------------------------------#
class ListadoSesionesFormacion(SuccessMessageMixin, CreateView, ListView):
    model = SesionesFormacion
    fields = "__all__"
    queryset = SesionesFormacion.objects.all()
    success_message = 'Roles creados satisfactoriamente'
    
    def get_success_url(self):        
        return reverse('principal3:leerSesionesFormacion')

class SesionesFormacionDetalle(DetailView):
    model = SesionesFormacion

class SesionesFormacionActualizar(SuccessMessageMixin, UpdateView):
    model = SesionesFormacion
    fields = "__all__"
    success_message = 'Roles actualizados satisfactoriamente'
    
    def get_success_url(self):               
        return reverse('principal3:leerSesionesFormacion')

class SesionesFormacionEliminar(SuccessMessageMixin, DeleteView): 
    model = SesionesFormacion
    
    def get_success_url(self): 
        success_message = 'Roles eliminados satisfactoriamente'
        messages.success(self.request, success_message)       
        return reverse('principal3:leerSesionesFormacion')
#---------------------------Fin de Vistas para Sesiones de Formacion-----------------------------------#