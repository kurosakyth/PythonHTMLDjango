from django.db import models

# Create your models here.
#captura la estructura la tabla libros en este caso
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to = 'images/', verbose_name='Imagen',null = True)
    descipcion = models.TextField(verbose_name='Descripcion', null = True)