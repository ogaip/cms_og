from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet

router = DefaultRouter()
router.register(r'articulos', ArticuloViewSet, basename="articulo")


urlpatterns = [
    path('', include(router.urls)),
]
