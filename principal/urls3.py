from django.contrib import admin
from django.urls import path
from principal.views3 import *

urlpatterns = [
    ##----------------------------------------------------------Crud Regiones---------------------------------------------------------------##
    path('Regiones/', ListadoRegiones.as_view(template_name="General/Regiones/tables.html"), name='leerRegiones'), 
    path('Regiones/detalle/<int:pk>', RegionesDetalle.as_view(template_name="General/Regiones/detalle.html"), name='detalleRegiones'),
    path('Regiones/editar/<int:pk>', RegionesActualizar.as_view(template_name="General/Regiones/actualizar.html"), name='actualizarRegiones'), 
    path('Regiones/eliminar/<int:pk>', RegionesEliminar.as_view(template_name='General/Regiones/eliminar.html')), 
    ##----------------------------------------------------------Fin Crud Regiones---------------------------------------------------------------##
    ##----------------------------------------------------------Crud Seguimientos---------------------------------------------------------------##
    path('Seguimientos/', ListadoSeguimientos.as_view(template_name="Otros/Seguimientos/tables.html"), name='leerSeguimientos'), 
    path('Seguimientos/detalle/<int:pk>', SeguimientosDetalle.as_view(template_name="Otros/Seguimientos/detalle.html"), name='detalleSeguimientos'),
    path('Seguimientos/editar/<int:pk>', SeguimientosActualizar.as_view(template_name="Otros/Seguimientos/actualizar.html"), name='actualizarSeguimientos'), 
    path('Seguimientos/eliminar/<int:pk>', SeguimientosEliminar.as_view(template_name='Otros/Seguimientos/eliminar.html')), 
    ##----------------------------------------------------------Fin Crud Seguimientos---------------------------------------------------------------##
    ##----------------------------------------------------------Crud Roles---------------------------------------------------------------##
    path('ProyectosActividades/', ListadoProyectosActividades.as_view(template_name="Listados/proyecto_actividad/tables.html"), name='leerProyectosActividades'), 
    path('ProyectosActividades/editar/<int:pk>', ProyectosActividadesActualizar.as_view(template_name="Listados/proyecto_actividad/actualizar.html"), name='actualizarProyectosActividades'), 
    path('ProyectosActividades/eliminar/<int:pk>', ProyectosActividadesEliminar.as_view(template_name='Listados/proyecto_actividad/eliminar.html')),
    ##----------------------------------------------------------Fin Crud Roles---------------------------------------------------------------#
    ##----------------------------------------------------------Crud Sesiones de Formacion---------------------------------------------------------------##
    path('SesionesFormacion/', ListadoSesionesFormacion.as_view(template_name="Otros/SesionesFormacion/tables.html"), name='leerSesionesFormacion'), 
    path('SesionesFormacion/detalle/<int:pk>', SesionesFormacionDetalle.as_view(template_name="Otros/SesionesFormacion/detalle.html"), name='detalleSesionesFormacion'),
    path('SesionesFormacion/editar/<int:pk>', SesionesFormacionActualizar.as_view(template_name="Otros/SesionesFormacion/actualizar.html"), name='actualizarSesionesFormacion'), 
    path('SesionesFormacion/eliminar/<int:pk>', SesionesFormacionEliminar.as_view(template_name='Otros/SesionesFormacion/eliminar.html')), 
    ##----------------------------------------------------------Fin Crud Sesiones de Formacion---------------------------------------------------------------##
]
