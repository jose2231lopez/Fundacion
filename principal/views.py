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
