# Proyecto Vehículos Django

# Descripción

Catálogo de vehículos que permite agregar y listar vehículos.

# Hitos de desarrolo

El proyecto se encuentra en desarrollo. 
- Se define el nombre "proyecto_vehiculos_django" para el directorio global del proyecto y el nombre "config" para el paquete principal del proyecto.
- Se crea la aplicación vehiculo para implementar las funcionalidades solicitadas.
- Se crea un formulario para agregar vehículos en `/vehiculo/add`.
- Se crea un cátalogo para listar los vehículos en `/vehiculo/list`.

# Instalación

1. Clonar el repositorio: `git clone https://github.com/bq-python-bootcamp-2024/proyecto_vehiculos_django.git`

2. (Opcional) Crear entorno para el proyecto: [Crear entorno con `virtualenvwrapper-win`](https://pypi.org/project/virtualenvwrapper-win/)
   
3.  Instalar las dependencias listadas en ["requirements.txt"](requirements.txt): `python -m pip install -r requirements.txt`

2. Copiar archivo .env con información protegida en el directorio principal del proyecto (enviado a la plataforma).

3. Poner en marcha el servidor de prueba: `python manage.py runserver`

# Endpoints (rutas) disponibles

## Endpoint: `/`
- **Método**: GET
- **Descripcion**: Página de inicio del cátalogo de vehículos
- **Response**: Retorna el contenido HTML de la página de inicio.
- **Ejemplos de Solicitud**:
  ```
  GET /
  ```
- **Respuesta**:
  - **200 OK**: La página de inicio se carga correctamente y devuelve el contenido HTML.

## Endpoint: `/vehiculo/add`
- **Método**: GET, POST
- **Descripcion**: Permite agregar un nuevo vehículo.
  - **GET**: Muestra un formulario para ingresar los detalles del vehículo.
  - **POST**: Envía el formulario para crear un nuevo registro de vehículo.
- **Campos del Formulario**:
  - `marca` (string, requerido): La marca del vehículo. Opciones: `Fiat`, `Chevrolet`, `Ford`, `Toyota`.
  - `modelo` (string, requerido): El modelo del vehículo.
  - `serial_carroceria` (string, requerido): El número de serie de la carrocería.
  - `serial_motor` (string, requerido): El número de serie del motor.
  - `categoria` (string, requerido): La categoría del vehículo. Opciones: `Particular`, `Transporte`, `Carga`.
  - `precio` (entero, requerido): El precio del vehículo.
- **Ejemplos de Solicitud**:
  - **GET**:
    ```
    GET /vehiculo/add/
    ```
  - **POST**:
    ```http
    POST /vehiculo/add/
    Content-Type: application/x-www-form-urlencoded

    marca=Toyota&modelo=Corolla&serial_carroceria=123ABC&serial_motor=456DEF&categoria=Particular&precio=20000
    ```
- **Respuesta**:
  - **200 OK**: Vehículo agregado exitosamente (redirecciona a la página principal o a la URL especificada).
  - **400 Bad Request**: Formulario inválido con mensajes de error (si faltan campos requeridos o contienen valores inválidos).