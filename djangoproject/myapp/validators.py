from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, RegexValidator

def validate_descripcion_required_with_imagen(value):
    if value.imagen and not value.descripcion:
        raise ValidationError("La descripción de la imagen es requerida si el campo de imagen está ocupado.")

def validate_positive_price(value):
    if value <= 0:
        raise ValidationError("El precio debe ser mayor a cero.")

def validate_identificacion(value):
    if len(value) == 10 or len(value) == 13:
        if value[:2] not in [str(i).zfill(2) for i in range(1, 25)]:
            raise ValidationError('La identificación debe comenzar con un número válido entre 01 y 24.')
    elif len(value) == 7:
        if not (value[0].isalpha() and value[1:].isdigit()):
            raise ValidationError('La identificación debe comenzar con una letra seguida de 6 números.')
    else:
        raise ValidationError('La identificación debe tener 7 para pasaporte, 10 para cédula o 13 para RUC caracteres.')

def validate_phone(value):
    if not ((value.startswith('09') and len(value) == 10) or
            ((value.startswith(('02', '03', '04', '05', '06', '07')) and len(value) == 9))):
        raise ValidationError('El número de teléfono debe tener 10 dígitos si empieza con 09 '
                              'y 9 dígitos si empieza con 02, 03, 04, 05, 06 o 07.')

def validate_city(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('La ciudad no puede contener números.')

def validate_provincia(value):
    provincias_ecuador = [
        'Azuay', 'Bolívar', 'Cañar', 'Carchi', 'Chimborazo', 'Cotopaxi', 'El Oro', 'Esmeraldas',
        'Galápagos', 'Guayas', 'Imbabura', 'Loja', 'Los Ríos', 'Manabí', 'Morona Santiago',
        'Napo', 'Orellana', 'Pastaza', 'Pichincha', 'Santa Elena', 'Santo Domingo de los Tsáchilas',
        'Sucumbíos', 'Tungurahua', 'Zamora Chinchipe'
    ]
    if value not in provincias_ecuador:
        raise ValidationError(f"La provincia debe ser una de las 24 provincias de Ecuador.")

def validate_country(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El país no puede contener números.')

def validate_ruc_length(value):
    if len(value) != 13:
        raise ValidationError('El RUC debe tener 13 dígitos.')

def validate_telefono(value):
    if not ((value.startswith('09') and len(value) == 10) or
            ((value.startswith(('02', '03', '04', '05', '06', '07')) and len(value) == 9))):
        raise ValidationError('El número de teléfono debe tener 10 dígitos si empieza con 09 '
                              'y 9 dígitos si empieza con 02, 03, 04, 05, 06 o 07.')

def validate_telegram_id(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError('El ID de Telegram debe ser un número de 10 dígitos.')

def validate_non_numeric_city(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('La ciudad no puede contener números.')

PAIS_CHOICES = [
        ('Ecuador', 'Ecuador'),
        ('Estados Unidos', 'Estados Unidos'),
        ('China', 'China'),
    ]