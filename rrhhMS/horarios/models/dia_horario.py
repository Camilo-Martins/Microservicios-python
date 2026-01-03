from django.db import models
from horario_semana import HorarioSemanal

class DiaHorario(models.Model):
    horario = models.ForeignKey(
        HorarioSemanal,
        on_delete=models.CASCADE,
        related_name="dias"
    )

    dia = models.IntegerField(
        choices=[
            (1, "Lunes"),
            (2, "Martes"),
            (3, "Miércoles"),
            (4, "Jueves"),
            (5, "Viernes"),
            (6, "Sábado"),
            (7, "Domingo"),
        ]
    )

    class Meta:
        unique_together = ("horario", "dia")
