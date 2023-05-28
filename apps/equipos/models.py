from django.db import models
from simple_history.models import HistoricalRecords
from apps.paises.models import Pais
from apps.ciudades.models import Ciudad
# Create your models here.

class Equipo(models.Model):
    Nombre = models.CharField(max_length=100, null= False)
    idCiudad = models.ForeignKey(Ciudad, null= True, blank= True, on_delete= models.CASCADE)


