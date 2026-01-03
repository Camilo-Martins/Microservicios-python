from django.db import models

# Create your models here.
class HorarioSemanal(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()  # lunes de la semana
    fecha_fin = models.DateField()     # domingo

    def __str__(self):
        return self.nombre
