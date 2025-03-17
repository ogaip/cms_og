from rest_framework.permissions import BasePermission


class IsOWnerOrReadOnly(BasePermission):
    """ 
    Permite la edicion solo si el usuario es el creador del objeto.
    Otros solo pueden leer (GET).
    """

    def tiene_permiso(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True

        return obj.user == request.user
