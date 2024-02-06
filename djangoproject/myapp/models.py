from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLES = [
        ('administrador', 'Administrador'),
        ('vendedor', 'Vendedor'),
    ]

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    rol = models.CharField(max_length=15, null=True, choices=ROLES)
    nombres_apellidos = models.CharField(null=True, max_length=100)
    cedula = models.CharField(null=True, max_length=10)
    direccion = models.CharField(null=True, max_length=100)
    telefono = models.CharField(null=True, max_length=10)
    referencia = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}-Profile'


class Categoria(models.Model):
    nombre = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre


class Imagen(models.Model):
    imagen = models.BinaryField()
    descripcion = models.CharField(max_length=50, null=True, blank=True)


class Producto(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    precioventa = models.DecimalField(max_digits=11, decimal_places=2)
    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=True)
    id_imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre


class Telegram(models.Model):
    id_telegram = models.CharField(primary_key=True, max_length=10)
    activo = models.BooleanField()
    telefono = models.CharField(max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    
class Cliente(models.Model):
    tipo_cliente = models.CharField(max_length=10)
    nombres_apellidos = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=13)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    referencia = models.CharField(max_length=50, null=True, blank=True)
    telegram = models.BooleanField(null=True)
    id_telegram = models.ForeignKey(Telegram, on_delete=models.SET_NULL, null=True)
    ciudad = models.CharField(max_length=20, null=True, blank=True)
    provincia = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nombres_apellidos


class Proveedor(models.Model):
    ruc_proveedor = models.CharField(max_length=13)
    Nombres = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    credito = models.BooleanField()
    Telefono = models.CharField(max_length=10)
    contacto_nombre_apellidos = models.CharField(
        max_length=100, null=True, blank=True)
    contacto_telefono = models.CharField(max_length=10, null=True, blank=True)
    contacto_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.Nombres


class Ingreso(models.Model):
    usuario = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    ruc_proveedor = models.CharField(max_length=13)
    n_comprobante = models.SmallIntegerField()
    fecha = models.DateField()
    IVA = models.SmallIntegerField()
    total = models.DecimalField(max_digits=11, decimal_places=2)


class DetalleIngreso(models.Model):
    ingreso = models.ForeignKey(Ingreso, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.SmallIntegerField()
    precio = models.DecimalField(max_digits=11, decimal_places=2)




class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
    id_telegram = models.ForeignKey(Telegram, on_delete=models.CASCADE, null=True)
    cantidad = models.SmallIntegerField()


class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    n_comprobante = models.SmallIntegerField()
    fecha = models.DateField()
    IVA = models.SmallIntegerField()
    total = models.DecimalField(max_digits=11, decimal_places=2)
    estado = models.CharField(max_length=20)
    forma_pago = models.CharField(max_length=20)


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.SET_NULL, null=True)
    producto = models.ForeignKey(
        Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.SmallIntegerField()
    precio = models.DecimalField(max_digits=11, decimal_places=2)
