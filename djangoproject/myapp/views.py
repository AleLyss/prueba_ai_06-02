from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import  ProveedorForm, ClienteForm, ProductoForm, EditProductoFormEdit, CreateUserForm, LoginForm, ProfileUpdateForm, UserUpdateForm,CategoriaForm
from django.http import JsonResponse
from .models import Proveedor, Cliente, Producto, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth, User
from .decorators import role_required
# Create your views here.

# MENUPRINCIPAL


@login_required(login_url="login")
def menuvista(request):

    return render(request, 'menuvista.html')
# REPORTES
def reportes(request):
     # Obtener los productos con stock igual a 1 o menor
    productos_menor_stock = Producto.objects.filter(stock__lte=1).order_by('stock')[:10]

    # Preparar los datos para la tabla
    nombres_stocks = [(producto.nombre, producto.stock) for producto in productos_menor_stock]

    # Pasar los datos a la plantilla
    context = {
        'nombres_stocks': nombres_stocks,
    }
    return render(request, 'reportes.html', context)


# PROVEEDOR
@role_required(allowed_roles=['administrador'])
def proveedores(request):
    return render(request, 'proveedores.html')


@role_required(allowed_roles=['administrador'])
def agregar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            # Reemplaza 'ruta_hacia_vista_correcta' con la ruta correcta
            return redirect('proveedores')
    else:
        form = ProveedorForm()

    context = {
        'form': form
    }
    return render(request, 'agregar_proveedor.html', context)


@role_required(allowed_roles=['administrador'])
def editar_proveedor(request, ruc_proveedor):
    proveedor = get_object_or_404(Proveedor, ruc_proveedor=ruc_proveedor)

    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('mostrar_proveedor', ruc_proveedor=ruc_proveedor)
    else:
        form = ProveedorForm(instance=proveedor)

    return render(request, 'editar_proveedor.html', {'form': form})




@role_required(allowed_roles=['administrador'])
def mostrar_proveedor(request, ruc_proveedor):
    proveedor = get_object_or_404(Proveedor, ruc_proveedor=ruc_proveedor)
    return render(request, 'mostrar_proveedor.html', {'proveedor': proveedor})


@role_required(allowed_roles=['administrador'])
def eliminar_proveedor(request, ruc_proveedor):
    proveedor = get_object_or_404(Proveedor, ruc_proveedor=ruc_proveedor)
    if request.method == 'POST':
        proveedor.delete()
        # Redirige a la lista de proveedors después de eliminar uno
        return redirect('proveedores')

    return render(request, 'eliminar_proveedor.html', {'proveedor': proveedor})


@role_required(allowed_roles=['administrador'])
def list_proveedor(_request):
    proveedores = list(Proveedor.objects.values())
    data = {'proveedores': proveedores}
    return JsonResponse(data)

# VENTA


@login_required(login_url="login")
def ventas(request):
    return render(request, 'ventas.html')

# CLIENTE


@login_required(login_url="login")
def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la lista de clientes después de crear uno nuevo
            return redirect('clientes')
    else:
        form = ClienteForm()

    return render(request, 'agregar_cliente.html', {'form': form})




@role_required(allowed_roles=['administrador'])
def eliminar_cliente(request, identificacion):
    cliente = get_object_or_404(Cliente, identificacion=identificacion)
    if request.method == 'POST':
        cliente.delete()
        # Redirige a la lista de clientes después de eliminar uno
        return redirect('clientes')

    return render(request, 'eliminar_cliente.html', {'cliente': cliente})


@login_required(login_url="login")
def mostrar_cliente(request, identificacion):
    cliente = get_object_or_404(Cliente, identificacion=identificacion)
    return render(request, 'mostrar_cliente.html', {'cliente': cliente})


@login_required(login_url="login")
def list_cliente(_request):
    clientes = list(Cliente.objects.values())
    data = {'clientes': clientes}
    return JsonResponse(data)


@login_required(login_url="login")
def buscar_cliente(_request, identificacion):
    cliente = get_object_or_404(Cliente, identificacion=identificacion)
    data = {
        'cliente': {
            'tipo_cliente': cliente.tipo_cliente,
            'nombres_apellidos': cliente.nombres_apellidos,
            'identificacion': cliente.identificacion,
            'direccion': cliente.direccion,
            'telefono': cliente.telefono,
            'email': cliente.email,
            'referencia': cliente.referencia,
            'telegram': cliente.telegram,
            'id_telegram': cliente.id_telegram,
            'ciudad': cliente.ciudad,
            'provincia': cliente.provincia
        }
    }
    return JsonResponse(data)


@login_required(login_url="login")
def editar_cliente(request, identificacion):
    cliente = get_object_or_404(Cliente, identificacion=identificacion)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('mostrar_cliente', identificacion=identificacion)
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'editar_cliente.html', {'form': form})


@login_required(login_url="login")
def clientes(request):
    return render(request, 'clientes.html')

# PRODUCTO


@login_required(login_url="login")
def productos(request):
    return render(request, 'productos.html')



@login_required(login_url="login")
def mostrar_producto(request, codigo_producto):
    producto = get_object_or_404(Producto, codigo=codigo_producto)

    return render(request, 'mostrar_producto.html', {'producto': producto})


@role_required(allowed_roles=['administrador'])
def eliminar_producto(request, codigo_producto):
    producto = get_object_or_404(Producto, codigo=codigo_producto)
    if request.method == 'POST':
        producto.delete()
        # Redirige a la lista de productos después de eliminar uno
        return redirect('productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})


@role_required(allowed_roles=['administrador'])
def editar_producto(request, codigo_producto):
    producto = get_object_or_404(Producto, codigo=codigo_producto)
    if request.method == 'POST':
        form = EditProductoFormEdit(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('mostrar_producto', codigo_producto=codigo_producto)
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'editar_producto.html', {'form': form, 'codigo_producto': codigo_producto})


@role_required(allowed_roles=['administrador'])
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            # Reemplaza 'ruta_hacia_vista_correcta' con la ruta correcta
            return redirect('productos')
    else:
        form = ProductoForm()

    context = {
        'form': form
    }
    return render(request, 'agregar_producto.html', context)


@login_required(login_url="login")
def list_producto(_request):
    productos = list(Producto.objects.values())
    data = {'productos': productos}
    return JsonResponse(data)


@login_required(login_url="login")
def buscar_producto(_request, codigo):
    producto = get_object_or_404(Producto, codigo=codigo)
    data = {
        'producto': {
            'codigo': producto.codigo,
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'stock': producto.stock,
            'precio': producto.precio,
            'precioventa': producto.precioventa,
            'id_categoria': producto.id_categoria
        }
    }
    return JsonResponse(data)


# usuariosistema
    # crear y registrar


def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("menuvista")

    context = {'loginform': form}

    return render(request, 'login.html', context=context)


def user_logout(request):
    auth.logout(request)

    return redirect("login")


@role_required(allowed_roles=['administrador'])
def profile(request):
    perfiles = Profile.objects.all()
    return render(request, 'profile.html', {'perfiles': perfiles})


@role_required(allowed_roles=['administrador'])
def list_profile(_request):
    profiles = list(Profile.objects.values())
    data = {'profiles': profiles}
    return JsonResponse(data)


@role_required(allowed_roles=['administrador'])
def editarprofile(request):
    user_found = None

    if request.method == 'POST':
        cedula = request.POST.get('cedula', '')
        
        # Buscar el perfil asociado a la cédula proporcionada
        try:
            profile = Profile.objects.get(cedula=cedula)
            user_found = {
                'user': profile.user,
                'profile': profile
            }
        except Profile.DoesNotExist:
            # Handle the case where no profile is found for the given cedula
            pass

    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()

    if user_found:
        if request.method == 'POST':
            # Si se envió el formulario de actualización, procesar la actualización
            user_form = UserUpdateForm(request.POST, instance=user_found['user'])
            profile_form = ProfileUpdateForm(request.POST, instance=user_found['profile'])

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('profile', username=user.username)
        else:
            # Si no se envió el formulario de actualización, mostrar la información actual del usuario
            user_form = UserUpdateForm(instance=user_found['user'])
            profile_form = ProfileUpdateForm(instance=user_found['profile'])

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_found': user_found
    }

    return render(request, 'editarprofile.html', context)

@role_required(allowed_roles=['administrador'])
def create_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST)
        profile_form = ProfileUpdateForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('profile-detail', username=user.username)
    else:
        user_form = UserUpdateForm()
        profile_form = ProfileUpdateForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'crearprofile.html', context)

def mostrar_profile(request):
    return render(request, 'mostrarusuario.html')