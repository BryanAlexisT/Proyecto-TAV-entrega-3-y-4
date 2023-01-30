# Generated by Django 3.2.8 on 2023-01-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='nuevoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreUsuario', models.CharField(max_length=16, verbose_name='nombreUsuario')),
                ('correo', models.CharField(max_length=50, verbose_name='correo')),
                ('password', models.CharField(max_length=12, verbose_name='password')),
            ],
        ),
    ]