from django import forms
from django.forms import ModelForm
from .models import Producto


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'precio', 'imagen', 'nombreCategoria']

