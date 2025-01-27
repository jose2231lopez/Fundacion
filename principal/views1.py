from django import apps
from django.shortcuts import render, redirect
from principal.models import *
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import *
from .models import Actividades 

def Login(request):

    return render(request, "login.html")

def Perfil(request):

    return render(request, "perfil.html")

def Home(request):

    return render(request, "GENERAL/index.html")

def Parametros1(request):

    return render(request, "GENERAL/index.html")

from django.apps import apps
from django.db.models import Q, Count
from django.shortcuts import render

def buscar_en_todas_las_tablas(request):
    query = request.GET.get('q', '').strip().lower()
    resultados = []
    reporte_proyectos = None
    reporte_beneficiarios = None
    reporte_actividades = None

    if query:
        modelos_a_buscar = [
            'Proyectos',
            'Beneficiarios',
            'Actividades',
            'Seguimientos',
            'Recursos',
            'Documentos',
        ]

        for modelo_nombre in modelos_a_buscar:
            try:
                modelo = apps.get_model('principal', modelo_nombre)
                fields = modelo._meta.fields

                # Dividir la consulta en palabras clave
                palabras = query.split()

                # Construir filtros
                filtros = Q()
                for palabra in palabras:
                    for field in fields:
                        if field.get_internal_type() in ['CharField', 'TextField']:
                            filtros |= Q(**{f"{field.name}__icontains": palabra})
                        elif field.get_internal_type() == 'IntegerField' and palabra.isdigit():
                            filtros |= Q(**{f"{field.name}": int(palabra)})

                # Filtrar los datos del modelo
                queryset = modelo.objects.filter(filtros)

                for obj in queryset:
                    datos_objeto = {
                        'campos': [],
                        'valores': [],
                    }
                    for field in fields:
                        field_name = field.verbose_name or field.name
                        value = getattr(obj, field.name, None)
                        datos_objeto['campos'].append(field_name)
                        datos_objeto['valores'].append(value)

                    resultados.append({
                        'tabla': modelo._meta.verbose_name,
                        'id': obj.pk,
                        'datos': datos_objeto,
                    })

                # Generar reportes específicos
                if modelo_nombre == 'Proyectos' and queryset.exists():
                    proyectos = modelo.objects.annotate(num_beneficiarios=Count('beneficiariosproyectos__beneficiario'))
                    mas_relevante = proyectos.order_by('-num_beneficiarios').first()
                    reporte_proyectos = {
                        'total': queryset.count(),
                        'mas_relevante': mas_relevante.nombre_proyecto if mas_relevante else None,
                        'proyectos': [
                            {
                                'nombre': proyecto.nombre_proyecto,
                                'num_beneficiarios': proyecto.num_beneficiarios,
                            }
                            for proyecto in proyectos
                        ],
                    }
                elif modelo_nombre == 'Beneficiarios' and queryset.exists():
                    masculino = modelo.objects.filter(genero='Masculino').count()
                    femenino = modelo.objects.filter(genero='Femenino').count()
                    reporte_beneficiarios = {
                        'total': queryset.count(),
                        'masculino': masculino,
                        'femenino': femenino,
                    }
                elif modelo_nombre == 'Actividades' and queryset.exists():
                    actividades = modelo.objects.annotate(num_proyectos=Count('proyectosactividades__proyecto'))
                    mas_relevante = actividades.order_by('-num_proyectos').first()
                    reporte_actividades = {
                        'total_actividades': queryset.count(),
                        'actividad_mas_relevante': mas_relevante.nombre_actividad if mas_relevante else None,
                        'actividades': [
                            {
                                'nombre': actividad.nombre_actividad,
                                'num_proyectos': actividad.num_proyectos,
                            }
                            for actividad in actividades
                        ],
                    }
            except LookupError:
                continue

    return render(request, 'resultados_busqueda.html', {
        'resultados': resultados,
        'query': query,
        'reporte_proyectos': reporte_proyectos,
        'reporte_beneficiarios': reporte_beneficiarios,
        'reporte_actividades': reporte_actividades,
    })

#Vista de el atajo para la tabla Documentos 
def crear_beneficiario(request):
    if request.method == 'POST':
        form = BeneficiarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El beneficiario se ha creado correctamente.')
            return redirect('principal2:leerProyectos')  
        else:
            messages.error(request, 'Hubo un error al crear el beneficiario.')
    else:
        form = BeneficiarioForm()
    return render(request, 'crear_beneficiario.html', {'form': form})

#---------------------------Vistas para Actividades-----------------------------------#
class ListadoActividades(SuccessMessageMixin, CreateView, ListView):
    model = Actividades
    fields = "__all__"
    queryset = Actividades.objects.all()
    success_message = 'Actividad creada satisfactoriamente'
    
    def get_success_url(self):        
        return reverse('principal1:leerActividades')

class ActividadesDetalle(DetailView):
    model = Actividades

class ActividadesActualizar(SuccessMessageMixin, UpdateView):
    model = Actividades
    fields = "__all__"
    success_message = 'Actividad actualizada satisfactoriamente'
    
    def get_success_url(self):               
        return reverse('principal1:leerActividades')

class ActividadesEliminar(SuccessMessageMixin, DeleteView): 
    model = Actividades
    
    def get_success_url(self): 
        success_message = 'Actividad eliminada satisfactoriamente' 
        messages.success(self.request, success_message)       
        return reverse('principal1:leerActividades')
#---------------------------Fin de Vistas para Actividades---------------------------------#    

#---------------------------Vistas para Beneficiarios-----------------------------------#
class ListadoBeneficiarios(SuccessMessageMixin, CreateView, ListView):
    model = Beneficiarios
    fields = "__all__"
    queryset = Beneficiarios.objects.all()
    success_message = 'Actividad creada satisfactoriamente'
    
    def get_success_url(self):        
        return reverse('principal1:leerActividades')

class BeneficiariosDetalle(DetailView):
    model = Beneficiarios

class BeneficiariosActualizar(SuccessMessageMixin, UpdateView):
    model = Beneficiarios
    fields = "__all__"
    success_message = 'Actividad actualizada satisfactoriamente'
    
    def get_success_url(self):               
        return reverse('principal1:leerBeneficiarios')

class BeneficiariosEliminar(SuccessMessageMixin, DeleteView): 
    model = Beneficiarios
    
    def get_success_url(self): 
        success_message = 'Beneficiario eliminada satisfactoriamente' 
        messages.success(self.request, success_message)       
        return reverse('principal1:leerBeneficiarios')
#---------------------------Fin de Vistas para Beneficiarios-------------------------#  
  
#---------------------------Vistas para Documentos-----------------------------------#
class ListadoDocumentos(SuccessMessageMixin, CreateView, ListView):
    model = Documentos
    fields = "__all__"
    queryset = Documentos.objects.all()
    success_message = 'Documento creado correctamente'
    
    def get_success_url(self):        
        return reverse('principal1:leerDocumentos')

class DocumentosDetalle(DetailView):
    model = Documentos

class DocumentosActualizar(SuccessMessageMixin, UpdateView):
    model = Documentos
    fields = "__all__"
    success_message = 'Documento actualizado correctamente'
    
    def get_success_url(self):               
        return reverse('principal1:leerDocumentos')

class DocumentosEliminar(SuccessMessageMixin, DeleteView): 
    model = Documentos
    
    def get_success_url(self): 
        success_message = 'Documento eliminado correctamente'
        messages.success(self.request, success_message)       
        return reverse('principal1:leerDocumentos')
    
#---------------------------Vistas para Beneficiarios_Proyectos------------------------------------#
class ListadoBeneficiariosProyectos(SuccessMessageMixin,ListView):
    model = BeneficiariosProyectos
    fields = "__all__"
    queryset = BeneficiariosProyectos.objects.all()
    
    def get_success_url(self):        
        return reverse('principal1:leerBeneficiariosProyectos')

class BeneficiariosProyectosActualizar(SuccessMessageMixin, UpdateView):
    model = BeneficiariosProyectos
    fields = "__all__"
    success_message = 'Documento actualizado correctamente'
    
    def get_success_url(self):               
        return reverse('principal1:leerBeneficiariosProyectos')
    
class BeneficiariosProyectosEliminar(SuccessMessageMixin, DeleteView):
    model = BeneficiariosProyectos

    def get_success_url(self): 
        success_message = 'Documento eliminado correctamente'
        messages.success(self.request, success_message)       
        return reverse('principal1:leerBeneficiariosProyectos')