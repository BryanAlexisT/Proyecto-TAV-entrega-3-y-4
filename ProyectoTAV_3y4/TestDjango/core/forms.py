from django import forms
from django.forms import ModelForm
from .models import Producto, nuevoUsuario


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'precio', 'imagen', 'nombreCategoria']

class UserForm(forms.ModelForm):
    
    class Meta:
        model = nuevoUsuario
        fields = ['nombreUsuario', 'correo', 'password']

