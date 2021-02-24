from django.db import models
from django.utils.timezone import now
# Importaré los usuarios registrados en el panel de administrador
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(
        verbose_name='Publicación', default=now)
    image = models.ImageField(verbose_name='Imagen',
                              upload_to='blog', null=True, blank=True)
    # ForeingKey me permite traer el valor para asignar el autor al usuario que crea la entrada.
    author = models.ForeignKey(
        User, verbose_name='Autor', on_delete=models.CASCADE)
    # on_delete: le indica qué hacer cuando borre el usuario.
    categories = models.ManyToManyField(Category, verbose_name='Categorías')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']

    def __str__(self):
        return self.title
