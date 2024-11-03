from django.urls import path
from . import views

urlpatterns = [
    # Rutas de la aplicación vehiculo
    # Ruta página de inicio  
    path('', views.index, name='index'),
    # Formulario agregar vehículos
    path('vehiculo/add/', views.agregar_vehiculo, name='agregar_vehiculo'),
    # Catálogo de vehículos
    path('vehiculo/list/', views.listar_vehiculo, name='listar_vehiculo'),

    # Rutas para gestión de sesiónes y usuarios
    # Formulario de registro de usuario
    path('register/', views.registrar_usuario, name='registrar_usuario'),
    # Formulario inicio de sesión
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    # Ruta para cerrar sesión
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
]