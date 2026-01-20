from django.db import models
from .dia_horario import DiaHorario
from personal.models import Empleado

class AsignacionDia(models.Model):
    dia = models.ForeignKey(
        DiaHorario,
        on_delete=models.CASCADE,
        related_name="asignaciones"
    )

    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("dia", "empleado")