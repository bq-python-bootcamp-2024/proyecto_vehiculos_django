from django.shortcuts import render, redirect

# Modelos y Formularios
from .forms import VehiculoForm

# Página de inicio
def index(request):
    context = {
        'titulo_documento': 'Catálogo de Vehículos',
        'titulo': 'Catálogo de Vehículos',
    }
    return render(request, 'index.html', context=context)

# Fórmulario que permite agregar vehículos
def agregar_vehiculo(request):
    # Método POST
    if request.method == 'POST':
        # Utilizar ModelForm del módelo Vehiculo
        # para validar los datos ingresados por el usuario
        form = VehiculoForm(request.POST)

        # Si los datos del formulario son válidos
        # guardamos el vehiculo en la base de datos
        if form.is_valid():
            form.save()
        return redirect('/vehiculo/add')

    # Método GET
    elif request.method == 'GET':
        # Crear un formulario vacío con Modelform del modelo Vehiculo
        form = VehiculoForm()
        context = {
            'titulo_documento': 'Agregar vehículo',
            'titulo': 'Agregar vehículo',
            'form': form
        }
        return render(request, 'agregar_vehiculo.html', context=context)