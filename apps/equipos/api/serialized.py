from rest_framework import serializers
from apps.equipos.models import Equipo


class EquipoSerialized(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'