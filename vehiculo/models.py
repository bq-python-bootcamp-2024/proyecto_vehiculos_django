from django.db import models

# Definir modelo Vehiculo con especificaciones solicitadas
class Vehiculo(models.Model):
    OPCIONES_MARCA = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]

    OPCIONES_CATEGORIA = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = models.CharField(max_length=20, choices=OPCIONES_MARCA, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=OPCIONES_CATEGORIA, default='Particular')
    precio = models.IntegerField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)