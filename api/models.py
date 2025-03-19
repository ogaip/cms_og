from django.db import models


class Articulo(models.Model):
    """
    Modelo que representa un artículo en el sistema CMS.

    Este modelo almacena la información básica de los artículos,
    incluyendo título, contenido y fechas de gestión.

    Atributos:
        titulo (CharField): Título del artículo, máximo 255 caracteres.
        contenido (TextField): Contenido completo del artículo.
        fecha_creacion (DateTimeField): Fecha y hora de creación del artículo.
        timestamp (DateTimeField): Fecha y hora de la última modificación.
    """

    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Devuelve una representación en string del artículo.

        Esta función es útil para mostrar el artículo en el admin de Django
        y en otros lugares donde se necesite una representación en texto.

        Returns:
            str: El título del artículo.
        """
        return str(self.titulo)

    class Meta:
        """
        Clase Meta para configurar propiedades del modelo.

        Define metadatos adicionales para el modelo Articulo.
        """
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        # Ordenar por fecha de creación, más reciente primero
        ordering = ['-fecha_creacion']
