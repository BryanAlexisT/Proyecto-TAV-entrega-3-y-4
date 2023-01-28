from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('/lgn', login, name="login"),
    path('/cont', contacto, name="contacto"),
    path('/inf', infoPublica, name="infoPublica"),
    path('/Pro1', Producto1, name="Producto1"),
    path('/Pro', Productos, name="Productos"),
    path('/reg', registrar, name="registrar"),
    path('/lis', listar, name="listar"),
    path('agr', agregar, name="agregar"),
    path('/mod', modificar, name="modificar"),
]