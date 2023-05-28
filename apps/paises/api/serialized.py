from rest_framework import serializers
from apps.paises.models import Pais

class PaisSerialized(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

