from django.forms import ModelForm, EmailField
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Vehiculo

# Definir Modelform de Vehiculo para generar un formulario
class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']

class FormularioRegistroUsuario(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user