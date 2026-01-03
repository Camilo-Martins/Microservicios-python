from django.db import models
from .empleado import Empleado

class Pago(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.IntegerField()
    pagado = models.BooleanField() 

    def __str__(self):
        return f"{self.empleado.nombre_completo} - {self.fecha} - ${self.monto}"

    class Meta:
        db_table='pago'
        verbose_name='Pago'
        verbose_name_plural='Pagos'
        unique_together = ("empleado", "fecha")
        ordering = ["-fecha"]