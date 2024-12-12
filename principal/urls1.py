from django.contrib import admin
from django.urls import path
from principal.views1 import *

urlpatterns = [ 
    ##--------------------------------------------------------------Crud Actividades---------------------------------------------------------------##
    path('Actividades/', ListadoActividades.as_view(template_name="General/Actividades/tables.html"), name='leerActividades'), 
    path('Actividades/detalle/<int:pk>', ActividadesDetalle.as_view(template_name="General/Actividades/detalle.html"), name='detalleActividades'),
    path('Actividades/editar/<int:pk>', ActividadesActualizar.as_view(template_name="General/Actividades/actualizar.html"), name='actualizarActividades'), 
    path('Actividades/eliminar/<int:pk>', ActividadesEliminar.as_view(template_name='General/Actividades/eliminar.html')), 
    ##--------------------------------------------------------------Fin Crud Actividades---------------------------------------------------------------##
    ##--------------------------------------------------------------Crud Beneficiarios---------------------------------------------------------------##
    path('Beneficiarios/', ListadoBeneficiarios.as_view(template_name = "General/Beneficiarios/tables.html"), name='leerBeneficiarios'), 
    path('Beneficiarios/detalle/<int:pk>', BeneficiariosDetalle.as_view(template_name = "General/Beneficiarios/detalle.html"), name='detalleBeneficiarios'),
    path('Beneficiarios/editar/<int:pk>',BeneficiariosActualizar.as_view(template_name = "General/Beneficiarios/actualizar.html"), name='actualizarBeneficiarios'), 
    path('Beneficiarios/eliminar/<int:pk>', BeneficiariosEliminar.as_view(template_name ='General/Beneficiarios/eliminar.html')),
    ##--------------------------------------------------------------Crud Beneficiarios---------------------------------------------------------------##
    ##--------------------------------------------------------------Crud Documentos---------------------------------------------------------------##
    path('Documentos/', ListadoDocumentos.as_view(template_name="General/Documentos/tables.html"), name='leerDocumentos'), 
    path('Documentos/detalle/<int:pk>', DocumentosDetalle.as_view(template_name="General/Documentos/detalle.html"), name='detalleDocumentos'),
    path('Documentos/editar/<int:pk>', DocumentosActualizar.as_view(template_name="General/Documentos/actualizar.html"), name='actualizarDocumentos'), 
    path('Documentos/eliminar/<int:pk>', DocumentosEliminar.as_view(template_name='General/Documentos/eliminar.html')), 
    ##--------------------------------------------------------------Fin Crud Documentos---------------------------------------------------------------##
    path('BeneficiariosProyectos/', ListadoBeneficiariosProyectos.as_view(template_name="Listados/beneficiario_proyecto/tables.html"), name='leerBeneficiariosProyectos'),
    path('BeneficiariosProyectos/editar/<int:pk>', BeneficiariosProyectosActualizar.as_view(template_name="Listados/beneficiario_proyecto/actualizar.html"), name='actualizarBeneficiariosProyectos'),
    path('BeneficiariosProyectos/eliminar<int:pk>',BeneficiariosProyectosEliminar.as_view(template_name='Listados/beneficiario_proyecto/eliminar.html')),
]
