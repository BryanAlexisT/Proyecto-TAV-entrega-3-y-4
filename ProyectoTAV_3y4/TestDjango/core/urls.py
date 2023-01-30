from django.urls import path
from .views import *
from django.conf import settings
from django.contrib.staticfiles.urls import static




urlpatterns = [
    path('', home, name="home"),
    path('/lgn', login, name="login"),
    path('/cont', contacto, name="contacto"),
    path('/inf', infoPublica, name="infoPublica"),
    path('/Pro1', Producto1, name="Producto1"),
    path('/Pro', Productos, name="Productos"),
    path('/reg', registrar, name="registrar"),
    path('/lis', listar, name="listar"),
    path('/agr', agregar, name="agregar"),
    path('mod/<id>', modificar, name="modificar"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)