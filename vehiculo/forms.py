from django.forms import ModelForm
from .models import Vehiculo

# Definir Modelform de Vehiculo para generar un formulario
class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']