from django.shortcuts import render
from principal.models import * 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages
from django import forms 
from django.contrib.auth import authenticate,get_user_model, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from .forms import *
# Funciones de vista simples
def Login(request):

    return render (request, "login.html")

def Perfil(request):
    
    return render (request, "perfil.html")

def home(request):
    
    return render (request, "index.html")

def parametros(request):

    return render(request,"nav.html")

def Home1(request):
    
    return render (request, "pagina fundacion/index.html")

def La_fundacion(request):
    
    return render (request, "pagina fundacion/La_fundacion.html")

def Contacto(request):
    
    return render (request, "pagina fundacion/Contacto.html")

def recover_password(request):
    
    return render(request, 'recover_password.html')

def index1(request):

    return render(request, 'index1')

"""
from django.apps import apps
from django.db.models import Q, Count
from django.shortcuts import render

#def buscar_en_todas_las_tablas(request):
    #query = request.GET.get('q', '').strip().lower()
    #resultados = []
    #reporte_proyectos = None
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

                # Procesar los Proyectos y contar beneficiarios 
                if (modelo_nombre == 'Proyectos' and queryset.exists()):
                    # Agregar los beneficiarios por proyecto sin utilizar tablas intermedias
                    proyectos_agrupados = modelo.objects.annotate(
                        num_beneficiarios=Count('beneficiario__beneficiario_id', distinct=True)
                    ).filter(num_beneficiarios__gt=0).order_by('-num_beneficiarios')

                    mas_relevante = proyectos_agrupados.first()

                    reporte_proyectos = {
                        'total': proyectos_agrupados.count(),
                        'mas_relevante': {
                            'nombre': mas_relevante['nombre_proyecto'],
                            'repeticiones': mas_relevante['conteo'],
                        } if mas_relevante else None,
                        'proyectos_duplicados': [
                            {
                                'nombre': proyecto['nombre_proyecto'],
                                'repeticiones': proyecto['conteo'],
                            }
                            for proyecto in proyectos_agrupados
                        ],
                    }
"""