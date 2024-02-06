from django import forms
from .models import Usuario, Proveedor, Cliente, Producto,Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Puedes personalizar los campos que quieres mostrar en el formulario


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        # Eliminar el atributo required para los campos id_categoria y id_imagen
        self.fields['id_categoria'].required = False
        self.fields['id_imagen'].required = False


class EditProductoFormEdit(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditProductoFormEdit, self).__init__(*args, **kwargs)
        self.fields['id_categoria'].required = False
        self.fields['id_imagen'].required = False
        self.fields['codigo'].widget.attrs['readonly'] = True

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
class UserUpdateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

