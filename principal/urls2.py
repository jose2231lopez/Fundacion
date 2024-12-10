from django.contrib import admin
from django.urls import path
from principal.views2 import *

urlpatterns = [
    ##----------------------------------------------------------Crud Donaciones---------------------------------------------------------------##
    path('Donaciones/', ListadoDonaciones.as_view(template_name="Otros/Donaciones/tables.html"), name='leerDonaciones'), 
    path('Donaciones/detalle/<int:pk>', DonacionesDetalle.as_view(template_name="Otros/Donaciones/detalle.html"), name='detalleDonaciones'),
    path('Donaciones/editar/<int:pk>', DonacionesActualizar.as_view(template_name="Otros/Donaciones/actualizar.html"), name='actualizarDonaciones'), 
    path('Donaciones/eliminar/<int:pk>', DonacionesEliminar.as_view(template_name='Otros/Donaciones/eliminar.html')), 
    ##----------------------------------------------------------Fin Crud Donaciones---------------------------------------------------------------##
    ##----------------------------------------------------------Crud Notificaciones---------------------------------------------------------------##
    path('Notificaciones/', ListadoNotificaciones.as_view(template_name="Otros/Notificaciones/tables.html"), name='leerNotificaciones'), 
    path('Notificaciones/detalle/<int:pk>', NotificacionesDetalle.as_view(template_name="Otros/Notificaciones/detalle.html"), name='detalleNotificaciones'),
    path('Notificaciones/editar/<int:pk>', NotificacionesActualizar.as_view(template_name="Otros/Notificaciones/actualizar.html"), name='actualizarNotificaciones'), 
    path('Notificaciones/eliminar/<int:pk>', NotificacionesEliminar.as_view(template_name='Otros/Notificaciones/eliminar.html')), 
    ##----------------------------------------------------------Fin Crud Notificaciones---------------------------------------------------------------##
    ##----------------------------------------------------------Crud Proyectos---------------------------------------------------------------##
    path('Proyectos/', ListadoProyectos.as_view(template_name="GENERAL/Proyectos/tables.html"), name='leerProyectos'), 
    path('Proyectos/detalle/<int:pk>', ProyectosDetalle.as_view(template_name="GENERAL/Proyectos/detalle.html"), name='detalleProyectos'),
    path('Proyectos/editar/<int:pk>', ProyectosActualizar.as_view(template_name="GENERAL/Proyectos/actualizar.html"), name='actualizarProyectos'), 
    path('Proyectos/eliminar/<int:pk>', ProyectosEliminar.as_view(template_name='GENERAL/Proyectos/eliminar.html')), 
    ##----------------------------------------------------------Fin Crud Proyectos---------------------------------------------------------------##
    ##----------------------------------------------------------Crud Recursos---------------------------------------------------------------##
    path('Recursos/', ListadoRecursos.as_view(template_name="Otros/Recursos/tables.html"), name='leerRecursos'), 
    path('Recursos/detalle/<int:pk>', RecursosDetalle.as_view(template_name="Otros/Recursos/detalle.html"), name='detalleRecursos'),
    path('Recursos/editar/<int:pk>', RecursosActualizar.as_view(template_name="Otros/Recursos/actualizar.html"), name='actualizarRecursos'), 
    path('Recursos/eliminar/<int:pk>', RecursosEliminar.as_view(template_name='Otros/Recursos/eliminar.html')), 
    ##----------------------------------------------------------Fin Crud Recursos---------------------------------------------------------------##
]