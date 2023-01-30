from django.db import models


# Create your models here.
class Categoria(models.Model):
    idCategoria =  models.IntegerField(primary_key = True, verbose_name = "Id de categoria")
    nombreCategoria = models.CharField(max_length = 25, verbose_name = "Nombre de la categoria")
    
    def __str__ (self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.CharField(max_length = 2, primary_key = True, verbose_name="idProducto")
    nombreProducto = models.CharField(max_length = 25, verbose_name="nombreProducto")
    precio = models.CharField(max_length = 6, null = True, blank = True, verbose_name="Precio") 
    imagen = models.ImageField(upload_to='core/MEDIA/', blank=False, null=True)
    nombreCategoria = models.ForeignKey('Categoria', verbose_name = "nombreCategoria", on_delete = models.CASCADE)
        
    def __str__ (self):
        return self.nombreProducto

class nuevoUsuario(models.Model):
    nombreUsuario = models.CharField(max_length=16, verbose_name = "nombreUsuario")
    correo = models.CharField(max_length=50, verbose_name = "correo")
    password = models.CharField(max_length=12, verbose_name="password")

    def __str__(self):
        return self.nombreUsuario

