from django.db import models

# Create your models here.
class HorarioSemanal(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()  # lunes de la semana
    fecha_fin = models.DateField()     # sabado de la misma semana
    is_active = models.BooleanField(default=True)
    admin_id = models.IntegerField(db_index=True)  # dueño / jefe (auth-ms)

    def __str__(self):
        return self.nombre

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["admin_id"],
                condition=models.Q(is_active=True),
                name="unique_active_horario_per_admin"
            )
        ]
        db_table='horario'
        verbose_name='Horario'
        verbose_name_plural='Horarios'