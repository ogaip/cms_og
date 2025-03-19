from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Articulo


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo User de Django.

    Permite la serialización y deserialización de objetos User,
    incluyendo operaciones CRUD con manejo especial de contraseñas.
    """

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'password'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validar_datos):
        """
        Crea y retorna una nueva instancia de User.

        Args:
            validar_datos (dict): Diccionario con los datos validados del usuario.

        Returns:
            User: Nueva instancia de usuario creada.
        """
        # password= validar_datos.pop('password')
        # user= User(**validar_datos)
        # user.set_password(password)
        # user.save()
        user = User.objects.create_user(**validar_datos)
        return user

    def update(self, instance, validar_datos):
        """
        Actualiza y retorna una instancia existente de User.

        Args:
            instance (User): Instancia existente del usuario.
            validar_datos (dict): Diccionario con los datos validados a actualizar.

        Returns:
            User: Instancia de usuario actualizada.
        """
        instance.username = validar_datos.get('username', instance.username)
        instance.email = validar_datos.get('email', instance.email)
        instance.first_name = validar_datos.get(
            'first_name', instance.first_name)
        instance.last_name = validar_datos.get('last_name', instance.last_name)

        password = validar_datos.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()
        return instance


class ArticuloSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo Articulo.

    Maneja la serialización y deserialización de artículos,
    incluyendo validaciones personalizadas para título y contenido.
    """

    class Meta:
        model = Articulo
        fields = '__all__'

    def validar_titulo(self, value):
        """
        Valida que el título del artículo tenga una longitud mínima.

        Args:
            value (str): Título del artículo a validar.

        Returns:
            str: Título validado.

        Raises:
            ValidationError: Si el título tiene menos de 5 caracteres.
        """
        if len(value) < 5:
            raise serializers.ValidationError(
                "el titulo debe tener al menos 5 caracteres.")
        return value

    def validar_contenido(self, value):
        """
        Valida que el contenido del artículo no esté vacío.

        Args:
            value (str): Contenido del artículo a validar.

        Returns:
            str: Contenido validado.

        Raises:
            ValidationError: Si el contenido está vacío.
        """
        if not value.strip():
            raise serializers.ValidationError(
                "el contenido no puede estar vacio.")
        return value
