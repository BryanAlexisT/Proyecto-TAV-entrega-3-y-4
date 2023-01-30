from pyexpat.errors import messages
from django.shortcuts import render,redirect
from .models import *
from django import forms
from .forms import ProductoForm, UserForm
# Create your views here.

def home(request):
    
    return render(request, 'core/index.html')

def login(request):
    datos = {
        'form' : UserForm()
    }
    if request.method=='POST':
        try:
            detalleUsuario=nuevoUsuario.objects.get(nombreUsuario=request.POST['usuario']=='BRYAN', password=request.POST['password'])=='bryxd596'
            print("usuario =", detalleUsuario)
            request.session['nombreUsuario']=detalleUsuario.nombreUsuario
            return render(request, 'core/listar.html')
        except nuevoUsuario.DoesNotExist as e:
            datos['mensaje'] = "nombre de usuario o contraseña no valido"



    elif request.method=='POST':
        try:
            detalleUsuario=nuevoUsuario.objects.get(nombreUsuario=request.POST['usuario'], password=request.POST['password'])
            print("usuario =", detalleUsuario)
            request.session['nombreUsuario']=detalleUsuario.nombreUsuario
            return render(request, 'core/indexuser.html')
        except nuevoUsuario.DoesNotExist as e:
            datos['mensaje'] = "nombre de usuario o contraseña no valido"
    return render(request, 'core/login.html')

def contacto(request):
    
    return render(request, 'core/contacto.html')

def infoPublica(request):
    
    return render(request, 'core/infoPublica.html')

def seguimiento(request):
    
    return render(request, 'core/seguimiento.html')

def Producto1(request):
    productos = Producto.objects.all()
    datos = {
        'productos' : productos
    }
    
    return render(request, 'core/producto1.html',datos)


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

def eliminar(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect(to="listar")

def modificar(request):
    producto = Producto.objects.get(idProducto=id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    return render(request, 'core/adm_modoficar.html',{'formulario': formulario})



def modificar(request,id):
    print("bandera1") 
    productos = Producto.objects.get(idProducto=id)
    datos = {
        'form' : ProductoForm(instance=productos)
    }
    print("bandera2") 
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES, instance=productos)
        print("bandera3") 
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/adm_modificar.html',datos)
