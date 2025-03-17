""" vista api """
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Articulo
from .serializers import ArticuloSerializer
from .permissions import IsOWnerOrReadOnly
# Create your views here.


class ArticuloViewSet(viewsets.ModelViewSet):
    """ aun no se bien """
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [IsOWnerOrReadOnly, IsAuthenticated]


# @api_view(['GET', 'POST'])
# def lista_articulos(request):
#     """ lista y crea articulos """
#     if request.method == 'GET':
#         articulos = Articulo.objects.all()
#         serializer = ArticuloSerializer(articulos, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = ArticuloSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
