"""
lista de routas para la API
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import ArticuloViewSet, UserViewSets

router = DefaultRouter()
router.register(r'articulos', ArticuloViewSet)
router.register(r'users', UserViewSets)


urlpatterns = [
    path('', include(router.urls)),
    # path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('token/verify/', TokenVerifyView.as_view(), name="token_verify"),
]
