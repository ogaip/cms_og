from django.db import models

# Create your models here.


class Articulo(models.Model):
    """ clase articulo """
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.titulo)
