from django.db import models
from simple_history.models import HistoricalRecords
# Create your models here.


class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True, null= False)
    history = HistoricalRecords()
    