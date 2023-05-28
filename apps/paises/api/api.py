from rest_framework import viewsets, permissions
from apps.paises.api.serialized import PaisSerialized
from apps.paises.models import Pais 


class ApiPais(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PaisSerialized
