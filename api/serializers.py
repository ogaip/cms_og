from rest_framework import serializers
from .models import Articulo


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = '__all__'  # incluye todos los campos

    def validar_titulo(self, value):
        """ valida que el titulo tenga mas de 5 caracteres """
        if len(value) < 5:
            raise serializers.ValidationError(
                "el titulo debe tener al menos 5 caracteres.")
        return value

    def validar_contenido(self, value):
        """ valida que el contenido no este vacio. """
        if not value.strip():
            raise serializers.ValidationError(
                "el contenido no puede estar vacio.")
        return value
