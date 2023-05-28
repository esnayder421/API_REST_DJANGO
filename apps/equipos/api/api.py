from rest_framework import viewsets, permissions
from apps.equipos.models import Equipo
from apps.equipos.api.serialized import EquipoSerialized


class ApiEqupos(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EquipoSerialized


