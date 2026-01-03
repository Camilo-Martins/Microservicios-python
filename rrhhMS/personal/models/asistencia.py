from django.db import models
from .empleado import Empleado

class Asistencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    asistio = models.BooleanField()

    registrado_por_admin = models.BooleanField(default=True)

    def __str__(self):
        estado = "Asistió" if self.asistio else "No asistió"
        return f"{self.empleado.nombre_completo} - {self.fecha} - {estado}"

    class Meta:
        db_table='asistencia'
        verbose_name='Asistencia'
        verbose_name_plural='Asistencias'
        unique_together = ("empleado", "fecha")