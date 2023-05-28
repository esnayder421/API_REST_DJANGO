from rest_framework import viewsets, permissions
from apps.ciudades.models import Ciudad
from apps.ciudades.api.serialized import CiudadSerialized


class apiCiudad (viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CiudadSerialized






