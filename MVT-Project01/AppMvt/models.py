from time import timezone
from django.db import models

# Create your models here.

#Una clase para dsp convertirlo en un dato en una BD 

class Miembro_Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
