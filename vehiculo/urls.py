from django.urls import path
from . import views

urlpatterns = [
    # Rutas de la aplicación vehiculo
    # Ruta página de inicio  
    path('', views.index, name='index'),
    # Formulario agregar vehículos
    path('vehiculo/add/', views.agregar_vehiculo, name='agregar_vehiculo'),
]