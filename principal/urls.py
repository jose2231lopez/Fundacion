from django.contrib import admin
from django.urls import path
from principal.views import *
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views,views1,views2,views3

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index1', views.index1, name='index1'),
    path('crear-actividad/', views2.crear_actividad, name='crearActividad'),
    path('crear-beneficiario/', views1.crear_beneficiario, name='crearBeneficiario'),
    path('crear-region/',views3.crear_region,name='crearRegion'),
]