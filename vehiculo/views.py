from django.shortcuts import render, redirect

# Manejo de sesiónes, usuarios y permisos
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Permisos
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required

# Modelos y formularios autenticación
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# Modelos y Formularios desarrollados
from .forms import FormularioRegistroUsuario
from .forms import VehiculoForm
from .models import Vehiculo

# Página de inicio
def index(request):
    context = {
        'titulo_documento': 'Catálogo de Vehículos',
        'titulo': 'Catálogo de Vehículos',
    }
    return render(request, 'index.html', context=context)

# Fórmulario que permite agregar vehículos
# Permitir acceso solo a usuarios autenticados
@login_required(login_url='/login')
def agregar_vehiculo(request):
    # Verificar que el usuario tenga el permiso necesario para agregar vehículos
    if not request.user.has_perm('vehiculo.add_vehiculo'):
        messages.error(request, 'No tiene acceso para agregar vehículos, redirigiendo...')
        # Si el usuario no tiene el permiso correspondiente se redirige al catálogo de vehículos
        # ya que por defecto un usuario comienza con permisos para visualizar el mismo.
        return redirect('/vehiculo/list')
    
    # Método POST
    if request.method == 'POST':
        # Utilizar ModelForm del módelo Vehiculo para validar los datos ingresados por el usuario
        form = VehiculoForm(request.POST)

        # Si los datos del formulario son válidos se guarda el vehiculo en la base de datos
        if form.is_valid():
            form.save()
            # Extra: Informar al usuario que se a registrado un nuevo vehículo
            messages.success(request, 'Se ha registrado exitosamente un nuevo vehículo.')
        else:
            # Extra: Informar al usuario que el registro ha fallado
            messages.error(request, 'El registro ha fallado. No se registro ningún vehículo.')
        
        # Redirigir al usuario nuevamente al formulario para agregar más vehículos
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

# Cátalogo de vehículos
# Permitir acceso solo a usuarios autenticados
@login_required(login_url='/login')
def listar_vehiculo(request):
    # Verificar que el usuario tenga el permiso necesario para ver el cátalogo de vehículos
    if not request.user.has_perm('vehiculo.visualizar_catalogo'):
        messages.error(request, 'No tiene acceso para visualizar catálogo de vehículos, redirigiendo...')
        # Si el usuario no tiene el permiso correspondiente se le redirige a la página de inicio
        # Por ejemplo cuando se crea un usuario a través del sitio administrativo
        # sin asignar permisos mínimos
        return redirect('/login')
    
    # Si se tiene acceso, se cargan los vehículos de la base de datos
    vehiculos = Vehiculo.objects.all()
    context = {
        'titulo_documento': 'Listado vehículos',
        'titulo': 'Listado vehículos',
        'vehiculos': vehiculos
    }
    return render(request, 'catalogo_vehiculos.html', context=context)

# Formulario registro de usuarios
def registrar_usuario(request):
    # Método POST
    if request.method == 'POST':
        form = FormularioRegistroUsuario(request.POST)
        # Caso en el que el formulario tiene errores
        if not form.is_valid():
            # Extra: Revisar si el usuario ya esta registrado
            if User.objects.filter(username=form.data['username']):
                # Extra: Informar al usuario y redirigir a iniciar sesión
                messages.error(request, 'El usuario ingresado ya se encuentra registrado. Puede iniciar sesión, redirigiendo...')
                return redirect('/login')
            else:
                # Si los datos son inválidos redirigir al usuario nuevamente al formulario
                messages.error(request, 'El registro de usuario ha fallado. Verifique que la información ingresada es correcta. Si ya esta registrado, puede iniciar sesión.')
                return redirect('/register')
        
        # Si no hay errores, guardar el usuario en la base de datos
        user = form.save()

        # Conceder permiso para visualizar el cátalogo
        contenttype_vehiculo = ContentType.objects.get_for_model(Vehiculo)
        permiso_visualizar_catalogo = Permission.objects.get(codename='visualizar_catalogo', content_type=contenttype_vehiculo)
        user.user_permissions.add(permiso_visualizar_catalogo)

        # Extra: Conceder permiso 'view_vehiculo' por defecto para facilitar
        # la habilitación de acceso al personal al sitio administrativo
        permiso_ver_vehiculo = Permission.objects.get(codename='view_vehiculo')
        user.user_permissions.add(permiso_ver_vehiculo)
        
        # Iniciar sesión
        login(request, user)
        
        # Extra: Mostrar mensaje de registro exitoso
        messages.success(request, 'Se ha registrado exitosamente.')

        # Redirigir al usuario al cátalogo de vehículos
        return redirect('/vehiculo/list')

    # Método GET
    elif request.method == 'GET':
        form = FormularioRegistroUsuario()
        context = {
            'titulo_documento': 'Registrarse',
            'titulo': 'Registrarse',
            'form': form, 
            'accion': 'Registrarse', 
            'comentario': 'Si ya estas registrado, puedes iniciar sesión',
            'enlace': '/login',
        }
        return render(request, 'formulario_sesion.html', context=context)

# Formulario inicio de sesión
def iniciar_sesion(request):
    # Método POST
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        # Caso en el que el formulario NO tiene errores
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(request, username=usuario, password=contrasena)

            # Si el usuario se ha autenticado correctamente
            if user is not None:
                # Iniciar sesión
                login(request, user)
                # Extra: Mostrar al usuario un mensaje de inicio de sesión exitoso
                messages.success(request, f'Ha iniciado sesión exitosamente como: {usuario}.')
                # Redirigir al catálogo de vehículos
                return redirect('/vehiculo/list')
        
        # Caso en el que el formulario tiene errores
        else:
            # Si los datos son inválidos redirigir al usuario nuevamente al formulario
            messages.error(request, f'Los datos ingresados no son válidos. Verifique la información ingresada. Si no esta registrado, puede registrarse para iniciar sesión.')
            return redirect('/login')
    
    # Método GET
    elif request.method == 'GET':
        # Si el usuario ya ha ingresado sesión previamente se redirige al cátalogo de vehículos
        if request.user.is_authenticated:
            # Extra: Informar al usuario que ya ha iniciado sesión
            messages.info(request, f'Ya ha iniciado sesión como: {request.user.username}, redirigiendo...')
            return redirect('/vehiculo/list')

        form = AuthenticationForm()
        context = {
            'titulo_documento': 'Iniciar sesión',
            'titulo': 'Iniciar sesión',
            'form': form, 
            'accion': 'Ingresar', 
            'comentario': 'Si no esta registrado aún, puede registrarse',
            'enlace': '/register'
        }
        return render(request, 'formulario_sesion.html', context=context)

def cerrar_sesion(request):
    # Cerrar sesión al usuario y redirigir a la página de inicio
    logout(request)
    # Extra: Informar el cierre de sesión exitoso
    messages.success(request, 'Ha cerrado sesión exitosamente, redirigiendo...')
    return redirect('/')