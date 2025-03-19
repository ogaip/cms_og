"""
Vistas de la API para el manejo de artículos.

Este módulo contiene las vistas basadas en ViewSets que proporcionan
la funcionalidad CRUD para los artículos del CMS.
"""
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .models import Articulo
from .serializers import ArticuloSerializer, UserSerializer
from .permissions import IsOWnerOrReadOnly


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ArticuloViewSet(viewsets.ModelViewSet):
    """
    ViewSet para ver y editar artículos.

    Este ViewSet proporciona automáticamente las acciones 'list', 'create',
    'retrieve', 'update' y 'destroy'.

    Atributos:
        queryset: Conjunto de todos los artículos disponibles.
        serializer_class: Clase serializadora para los artículos.
        permission_classes: Lista de permisos requeridos para acceder a las vistas.
    """
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.IsAuthenticated]
