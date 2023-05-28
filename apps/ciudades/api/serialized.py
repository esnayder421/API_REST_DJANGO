from rest_framework import serializers
from apps.ciudades.models import Ciudad


class CiudadSerialized(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'





