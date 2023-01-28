from django.shortcuts import render,redirect
from .models import Producto
from django import forms
from .forms import ProductoForm
# Create your views here.

def home(request):
    
    return render(request, 'core/index.html')

def login(request):
    
    return render(request, 'core/login.html')

def contacto(request):
    
    return render(request, 'core/contacto.html')

def infoPublica(request):
    
    return render(request, 'core/infoPublica.html')

def Producto1(request):
    
    return render(request, 'core/Producto1.html')

def Productos(request):
    
    return render(request, 'core/Productos.html')

def registrar(request):
    
    return render(request, 'core/registrar.html')

def listar(request):
    productos = Producto.objects.all()
    datos = {
        'productos' : productos
    }
    
    return render(request, 'core/adm_listar.html',datos)


def agregar(request):
    datos = {
        'form' : ProductoForm()
    }
    print("bandera1")

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        print(request.POST)
        print("bandera2") 
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"
            print("bandera3")
    return render(request, 'core/adm_agregar.html', datos)



def modificar(request, id):
    productos = Producto.objects.get(idProducto=id)
    datos = {
        'form' : ProductoForm(instance=productos)
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=productos)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/adm_modificar', datos)
