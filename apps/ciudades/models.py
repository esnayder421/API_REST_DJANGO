from django.db import models
from simple_history.models import HistoricalRecords
from apps.paises.models import Pais
# Create your models here.



class Ciudad(models.Model):
    Nombre = models.CharField(max_length=100, null= False)
    history = HistoricalRecords()
    idPais = models.ForeignKey(Pais, null= True, blank= True, on_delete= models.CASCADE)

