from django.db import models
from dia_horario import DiaHorario
from ...personal.models.empleado import UserMetaData

class AsignacionDia(models.Model):
    dia = models.ForeignKey(
        DiaHorario,
        on_delete=models.CASCADE,
        related_name="asignaciones"
    )

    empleado = models.ForeignKey(
        UserMetaData,
        on_delete=models.PROTECT
    )

    class Meta:
        unique_together = ("dia", "empleado")