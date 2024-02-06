from django.db import models
from .validators import *

class Categoria(models.Model):
    nombre = models.CharField(max_length=25)

class Imagen(models.Model):
    imagen = models.BinaryField()
    descripcion = models.CharField(max_length=50, null=True)

    def clean(self):
        super().clean()
        validate_descripcion_required_with_imagen(self)

class Producto(models.Model):
    codigo = models.CharField(max_length=50, null=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, null=True)
    stock = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=11, decimal_places=2)

    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_imagen = models.ForeignKey(Imagen, on_delete=models.CASCADE)

    def clean(self):
        super().clean()
        validate_positive_price(self.precio)

class Detalle_Venta(models.Model):
    id_venta = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField()
    precio = models.DecimalField(max_digits=11, decimal_places=2)

    def clean(self):
        super().clean()
        validate_positive_price(self.precio)
        
class Venta(models.Model):
    id_cliente = models.IntegerField()
    id_usuario = models.IntegerField()
    n_comprobante = models.PositiveSmallIntegerField()
    fecha = models.DateField()
    IVA = models.PositiveSmallIntegerField()
    total = models.DecimalField(max_digits=11, decimal_places=2)
    estado = models.CharField(max_length=20)

class Cliente(models.Model):
    tipo_cliente = models.CharField(max_length=10, choices=(('natural', 'Natural'), ('juridico', 'Jurídico')))
    nombres_apellidos = models.CharField(max_length=100)
    identificacion = models.CharField(max_length=13)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, validators=[validate_phone])
    email = models.EmailField()
    referencia = models.CharField(max_length=50, null=True)
    telegram = models.BooleanField()
    id_telegram = models.CharField(max_length=10, null=True, validators=[validate_telegram_id])
    ciudad = models.CharField(max_length=20, null=True, validators=[validate_non_numeric_city])
    provincia = models.CharField(max_length=20, null=True, validators=[validate_provincia])

class Rol(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)

class Usuario(models.Model):
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    nombres_apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, validators=[validate_phone])
    email = models.EmailField()
    referencia = models.CharField(max_length=50, null=True)
    clave = models.BinaryField()

class Ingreso(models.Model):
    id_usuario = models.IntegerField()
    id_proveedor = models.IntegerField()
    ruc_proveedor = models.CharField(max_length=13, validators=[validate_ruc_length])
    n_comprobante = models.PositiveSmallIntegerField()
    fecha = models.DateField()
    IVA = models.PositiveSmallIntegerField()
    total = models.DecimalField(max_digits=11, decimal_places=2)

class Proveedor(models.Model):
    ruc_proveedor = models.CharField(max_length=13, validators=[validate_ruc_length])
    tipo = models.CharField(max_length=20, choices=(('natural', 'Natural'), ('juridico', 'Jurídico')))
    ciudad = models.CharField(max_length=20, null=True, validators=[validate_city])
    pais = models.CharField(max_length=20, choices=PAIS_CHOICES, validators=[validate_country])
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    credito = models.BooleanField()
    Telefono = models.CharField(max_length=10, validators=[validate_telefono])
    contacto_nombre_apellidos = models.CharField(max_length=100, null=True)
    contacto_telefono = models.CharField(max_length=10, null=True, validators=[validate_telefono])
    contacto_email = models.EmailField(null=True)
    

class Detalle_Ingreso(models.Model):
    id_ingreso = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField()
    precio = models.DecimalField(max_digits=11, decimal_places=2)

    def clean(self):
        super().clean()
        validate_positive_price(self.precio)

class Telegram(models.Model):
    id_telegram = models.CharField(max_length=10, primary_key=True, validators=[validate_telegram_id])
    activo = models.BooleanField()
    telefono = models.CharField(max_length=10, validators=[validate_telefono])
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

class Carrito(models.Model):
    id_cliente = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_telegram = models.ForeignKey(Telegram, on_delete=models.CASCADE)
    cantidad = models.PositiveSmallIntegerField()