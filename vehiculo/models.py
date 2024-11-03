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

    def __str__(self):
        return f'Vehículo {self.categoria}: {self.marca} {self.modelo} (${self.precio})'
    
    # Extra: Configurar nombres visibles del modelo
    # Extra: Ordenar por precio de forma ascendente
    # Crear permiso 'visualizar_catalogo'
    class Meta:
        verbose_name = 'vehículo'
        verbose_name_plural = 'vehículos'
        ordering = ['precio']
        permissions = (('visualizar_catalogo', 'Permite a un usuario visualizar el catálogo de vehículos'),)

    # Crear un campo dinámico en base al precio
    def condicion_de_precio(self):
        if self.precio >= 0 and self.precio <= 10000:
            return 'Bajo'
        elif self.precio > 10000 and self.precio <= 30000:
            return 'Medio'
        elif self.precio > 30000:
            return 'Alto'